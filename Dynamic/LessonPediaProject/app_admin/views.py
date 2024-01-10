from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.utils import timezone
from .models import AppAdmin
from client.models import Client
from tutor.models import Tutor
from .backends import AppAdminAuthBackend
from .serializers import ClientSerializer, TutorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
import hashlib
import uuid
from generic_apps.models import ClientReportAbuse, TutorReportAbuse
from generic_apps.serializers import ClientReportAbuseSerializer, TutorReportAbuseSerializer
from django.core.mail import send_mail

def landing_page_admin(request):
    """Landing page"""
    return render(request, "app_admin/landingpage_admin.html")


# def generate_browser_fingerprint(request):
#     """Generate a unique fingerprint based on browser information"""
#     user_agent = request.META.get('HTTP_USER_AGENT', '').encode()
#     ip_address = request.META.get('REMOTE_ADDR', '').encode()

#     fingerprint = hashlib.sha256((user_agent + ip_address)).hexdigest()
#     return fingerprint

def generate_browser_fingerprint(request):
    """Generate a unique fingerprint based on a UUIDv4"""
    random_uuid = uuid.uuid4().hex.encode()
    
    fingerprint = hashlib.sha256(random_uuid).hexdigest()
    return fingerprint

def app_admin_login(request):
    """Login view for admin"""
    if request.method == 'POST':
        # Check if another admin is already logged in from the same browser
        existing_fingerprint = request.session.get('browser_fingerprint')
        if existing_fingerprint:
            messages.error(request, "An Admin is currently logged in on this browser")
            return redirect('app_admin_sign_up')

        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        AppAdminAuth = AppAdminAuthBackend()
        user = AppAdminAuth.authenticate(request, username=username_or_email, password=password)
        if user is not None:
            # Generate browser fingerprint
            browser_fingerprint = generate_browser_fingerprint(request)
            # Check if another admin logged in from the same browser
            if request.session.get('browser_fingerprint') and request.session.get('browser_fingerprint') != browser_fingerprint:
                logout(request)
                messages.error(request, "An Admin is currently logged in on this browser")
                return redirect('app_admin_sign_up')


            login(request, user, backend='app_admin.backends.AppAdminAuthBackend')
            request.session['logged_in'] = True  # Set a session variable
            request.session['account_type'] = 'admin'  # Set the user type in the session
            request.session['browser_fingerprint'] =browser_fingerprint
            return redirect('app_admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return redirect('app_admin_sign_up')


# @login_required(login_url='app_admin_sign_up')
# def app_admin_dashboard(request):
#     """"""
#     if request.user.is_authenticated:
#         account_type = 'admin'  # Assuming this is how you determine the account type

#         return render(request, 'app_admin/admin_dashboard.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required(login_url='app_admin_sign_up')
def app_admin_dashboard(request):
    """Basic admin dashboard logics"""
    if request.user.is_authenticated:
        account_type = 'admin'  # Assuming this is how you determine the account type

        all_tutors = Tutor.objects.all()
        all_clients = Client.objects.all()

        return render(request, 'app_admin/admin_dashboard.html', {'tutors': all_tutors, 'clients': all_clients})



@login_required(login_url='app_admin_sign_up')
def app_admin_logout(request):
    """admin logout logics"""
    # Clear the session variable and log the user out
    if 'logged_in' in request.session:
        del request.session['logged_in']
    if 'account_type' in request.session:
        del request.session['account_type']
    
    logout(request)
    return redirect('app_admin_sign_up')


@login_required(login_url='app_admin_sign_up')
def get_admin_username(request):
    """get admin username basic api"""
    if request.user.is_authenticated:
        username = request.user.username
        return JsonResponse({'username': username})
    else:
        return JsonResponse({'username': 'Admin'})


@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_tutors_data(request):
    """ get tutor data api using django rest framwork"""
    if request.method == 'GET':
        tutors_data = Tutor.objects.all()

        # return JsonResponse({'tutors': tutors_data })


        # Serialize tutor data using the serializer
        tutors_data_serialized = TutorSerializer(tutors_data, many=True)
        
        return Response({
            'tutors_data': tutors_data_serialized.data  # Serialized tutor data
        }, status=status.HTTP_200_OK)
    

# Tutor Logics

# @login_required(login_url='app_admin_sign_up')
# def get_tutor_count(request):
#     """ get tutor count api """
#     if request.method == 'GET':
#         tutor_count = Tutor.objects.count()
#         return JsonResponse({'tutor_count': tutor_count})
    

@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_tutor_count(request):
    """get tutor count using django RF """
    if request.method == 'GET':
        tutor_count = Tutor.objects.count()
        return Response({'tutor_count': tutor_count}, status=status.HTTP_200_OK)


@login_required(login_url='app_admin_sign_up')
def get_nos_active_tutors(request):
    """get number of active tutor using basic api"""
    if request.method == 'GET':
        active_tutor_count = Tutor.objects.filter(is_active=True).count()
        return JsonResponse({'active_tutor_count': active_tutor_count})


@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_nos_inactive_tutors(request):
    """get number of inactive tutors django RF """
    if request.method == 'GET':
        inactive_tutor_count = Tutor.objects.filter(is_active=False).count()
        return Response({'inactive_tutor_count': inactive_tutor_count}, status=status.HTTP_200_OK)



# clients logics
    
@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_clients_data(request):
    """ get tutor data api using django rest framwork"""
    if request.method == 'GET':
        client_data = Client.objects.all()

        # return JsonResponse({'tutors': tutors_data })


        # Serialize tutor data using the serializer
        clients_data_serialized = ClientSerializer(client_data, many=True)
        
        return Response({
            'clients_data': clients_data_serialized.data  # Serialized tutor data
        }, status=status.HTTP_200_OK)

@login_required(login_url='app_admin_sign_up')
def get_client_count(request):
    """get client count basic api """
    if request.method == 'GET':
        client_count = Client.objects.count()
        return JsonResponse({'client_count': client_count})
    

@login_required(login_url='app_admin_sign_up')
def get_nos_active_clients(request):
    """get number of active clients using basic api"""
    if request.method == 'GET':
        active_client_count = Client.objects.filter(is_active=True).count()
        return JsonResponse({'active_client_count': active_client_count})


@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_nos_inactive_clients(request):
    """get number of inactive clients django RF """
    if request.method == 'GET':
        inactive_client_count = Client.objects.filter(is_active=False).count()
        return Response({'inactive_client_count': inactive_client_count}, status=status.HTTP_200_OK)
    

# Tutor and client suspension logics

# Tutor suspension logics

# @api_view(['POST'])
# @login_required(login_url='app_admin_sign_up')
# def suspend_tutor(request, tutor_id):
#     try:
#         tutor = Tutor.objects.get(pk=tutor_id)
#         tutor.is_active = False
#         tutor.save()
#         return Response({'message': 'Tutor suspended successfully'}, status=status.HTTP_200_OK)
#     except Tutor.DoesNotExist:
#         return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Tutor suspension/blocking/reactivation/deleting  logics
class TutorViewSet(ModelViewSet):
    """Tutor viewset"""
    permission_classes = [IsAuthenticated] # Sets the permission class for the viewset

    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

    @action(detail=True, methods=['POST'])
    def deactivate_tutor(self, request, pk=None):
        """Deactivate (block) tutor method"""
        try:
            tutor = Tutor.objects.get(pk=pk)
            tutor.is_active = False
            tutor.is_blocked_admin = True
            tutor.blocked_at_admin = timezone.now()
            tutor.block_reason_admin = request.data['block_reason']
            tutor.save()
            return Response({'message': 'Tutor suspended successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)                                                                                                                                                    

    
    @action(detail=True, methods=['POST'])
    def activate_tutor(self, request, pk=None):
        """Reactivate tutor method"""
        try:
            tutor = Tutor.objects.get(pk=pk) #works
            # tutor = self.get_object() # works too
            tutor.is_active = True
            tutor.is_blocked_admin = False
            tutor.is_suspended_admin = False
            tutor.suspension_duration_admin = None
            tutor.suspension_reason_admin = None
            tutor.block_reason_admin = None
            tutor.suspended_at_admin = None
            tutor.blocked_at_admin = None
            tutor.is_suspended = False
            tutor.is_blocked = False
            tutor.save()
            return Response({'message': 'Tutor activated successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)  



    @action(detail=True, methods=['POST'])
    def suspend_tutor(self, request, pk=None):
        """suspend tutor method"""
        try:
            tutor = Tutor.objects.get(pk=pk)
            # tutor = self.get_object()
            tutor.is_active = False
            tutor.is_suspended_admin = True
            tutor.suspended_at_admin = timezone.now()
            tutor.suspension_duration_admin = request.data['suspension_duration']
            tutor.suspension_reason_admin = request.data['suspension_reason']
            tutor.save()
            return Response({'message': 'Tutor suspended successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)                                                                                                                                                 


    @action(detail=True, methods=['DELETE'])
    def delete_tutor(self, request, pk=None):
        """delete tutor method"""
        try:
            tutor = Tutor.objects.get(pk=pk)
            # tutor = self.get_object()
            confirmation = request.data['confirmation']
            if confirmation == 'CONFIRM DELETE':
                tutor.delete()
                return Response({'message': 'Tutor deleted successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Tutor not deleted, please type in the right confirmation text'}, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'message': 'Tutor not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)






# # Client suspension/blocking/reactivation/deleting logics
class ClientViewSet(ModelViewSet):
    """Client viewset"""
    permission_classes = [IsAuthenticated] # Sets the permission class for the viewset

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=['POST'])
    def deactivate_client(self, request, pk=None):
        """Deactivate (block) client method"""
        try:
            # client = Client.objects.get(pk=pk)
            client = self.get_object()
            client.is_active = False
            client.is_blocked_admin = True
            client.block_reason_admin = request.data['block_reason']
            client.blocked_at_admin = timezone.now()
            client.save()
            return Response({'message': 'Client account deactivated (blocked) successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    


    @action(detail=True, methods=['POST'])
    def activate_client(self, request, pk=None):
        """Reactivate client method"""
        try:
            # client = Client.objects.get(pk=pk)
            client = self.get_object()

            client.is_active = True
            client.deactivateByClient = True
            client.is_blocked_admin = False
            client.is_suspended_admin = False
            client.suspension_duration_admin = None
            client.suspension_reason_admin = None
            client.block_reason_admin = None
            client.suspended_at_admin = None
            client.blocked_at_admin = None
            client.save()
            return Response({'message': 'Client activated successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def suspend_client(self, request, pk=None):
        """delete client method"""
        try:
            # client = Client.objects.get(pk=pk)
            client = self.get_object()
            client.is_active = False
            client.is_suspended_admin = True
            client.suspended_at_admin = timezone.now()
            client.suspension_duration_admin = request.data['suspension_duration']
            client.suspension_reason_admin = request.data['suspension_reason']
            client.save()
            return Response({'message': 'Client suspended successfully'}, status=status.HTTP_200_OK)
        except Http404:
            return Response({'message': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=True, methods=['DELETE'])
    def delete_client(self, request, pk=None):
        """delete client method"""
        try:
            # client = Client.objects.get(pk=pk)
            client = self.get_object()
            confirmation = request.data['confirmation']
            if confirmation == 'CONFIRM DELETE':
                client.delete()
                return Response({'message': 'Client deleted successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Client not deleted, please type in the right confirmation text'}, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'message': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        



class AppAdminTutorsReportViewSet(ModelViewSet):
    """AppAdmin Report Abuse viewset for related api logics"""

    permission_classes = [IsAuthenticated]

    queryset = TutorReportAbuse.objects.all()
    serializer_class = TutorReportAbuseSerializer

    @action(detail=True, methods=['post'])
    def update_report_status(self, request, pk=None):
        """Update tutor report status"""
        tutor_report = self.get_object()
        report_status = request.data['report_status'] # True or False, actually the resolved_by_admin field
        
        try:
            if report_status == "true":
                tutor_report.resolved_by_admin = False
                tutor_report.resolved_at = None
                tutor_report.save()
                return Response({'message': 'Tutor report resolve status updated successfully'}, status=status.HTTP_200_OK)
            
            elif report_status == "false":
                tutor_report.resolved_by_admin = True
                tutor_report.resolved_at = timezone.now()
                tutor_report.save()
                return Response({'message': 'Tutor report resolve status updated successfully'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'Invalid status on resolved by Admin'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'message': 'Error updating tutor report status'}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['post'])
    def send_email_for_tutor_report(self, request, pk=None):
        tutor_report_obj = self.get_object()
        created_at = tutor_report_obj.created_at
        report_id = tutor_report_obj.id
        report_subject = tutor_report_obj.subject
        report_message = tutor_report_obj.message
        target_client_id = tutor_report_obj.target_client_id.id
        tutor_id = tutor_report_obj.tutor.id
        
        # to be used for email formating
        tutor_obj = Tutor.objects.get(pk=tutor_id)
        tutor_serializer = TutorSerializer(tutor_obj)
        serialized_tutor = tutor_serializer.data
        tutor_email = serialized_tutor['email']

        reported_client_obj = Client.objects.get(pk=target_client_id)
        clients_serializer = ClientSerializer(reported_client_obj)
        serialized_client = clients_serializer.data
        client_firstname = serialized_client.get('first_name')
        client_lastname = serialized_client['last_name']
        client_fullname = f"{client_firstname} {client_lastname}"


        try:
            message_who = request.data['message_who']

            if message_who == 'tutor':
                message_body = request.data['message']
                subject = "Response to your report"

                sender = 'adminlessonpedia@gmail.com'
                recipient = 'andrewetedu@gmail.com' # tutor_email
                message = f"{message_body}\n\n{sender}"
                # print(message)

                send_mail(subject, message, sender, [recipient])
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
            
            elif message_who == 'client':
                message_body = request.data['message']
                subject = "Please respond within 2 days"

                sender = 'adminlessonpedia@gmail.com'
                recipient = 'andrewetedu@gmail.com' # client_email
                message = f"{message_body}\n\n{sender}"
                # print(message)

                send_mail(subject, message, sender, [recipient])
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error sending email', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class AppAdminClientReportViewSet(ModelViewSet):
    """AppAdmin Report Abuse viewset for related api logics"""

    permission_classes = [IsAuthenticated]

    queryset = ClientReportAbuse.objects.all()
    serializer_class = ClientReportAbuseSerializer

    @action(detail=True, methods=['post'])
    def update_report_status(self, request, pk=None):
        """Update client report status"""
        client_report = self.get_object()
        report_status = request.data['report_status'] # True or False, actually the resolved_by_admin field
        
        try:
            if report_status == 'true':
                client_report.resolved_by_admin = False
                client_report.resolved_at = None
                client_report.save()
                return Response({'message': 'Client report resolve status updated successfully'}, status=status.HTTP_200_OK)
            
            elif report_status == 'false':
                client_report.resolved_by_admin = True
                client_report.resolved_at = timezone.now()
                client_report.save()
                return Response({'message': 'Client report resolve status updated successfully'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'Invalid status on resolved by Admin'}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({'message': 'Error updating client report status'}, status=status.HTTP_400_BAD_REQUEST)
        


    @action(detail=True, methods=['post'])
    def send_email_for_client_report(self, request, pk=None):
        client_report_obj = self.get_object()
        created_at = client_report_obj.created_at
        report_id = client_report_obj.id
        report_subject = client_report_obj.subject
        report_message = client_report_obj.message
        target_tutor_id = client_report_obj.target_tutor.id
        client_id = client_report_obj.client.id
        

        # to be used for email formating
        client_obj = Client.objects.get(pk=client_id)
        client_serializer = ClientSerializer(client_obj)
        serialized_client = client_serializer.data
        client_email = serialized_client['email']

        reported_tutor_obj = Tutor.objects.get(pk=target_tutor_id)
        tutors_serializer = TutorSerializer(reported_tutor_obj)
        serialized_tutor = tutors_serializer.data
        tutor_firstname = serialized_tutor.get('first_name')
        tutor_lastname = serialized_tutor['last_name']
        tutor_fullname = f"{tutor_firstname} {tutor_lastname}"       
        try:
            message_who = request.data['message_who']

            if message_who == 'client':
                message_body = request.data['message']
                subject = "Response to your report"

                sender = 'adminlessonpedia@gmail.com'
                recipient = 'andrewetedu@gmail.com' # client_email
                message = f"{message_body}\n\n{sender}"
                # print(message)

                send_mail(subject, message, sender, [recipient])
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
            
            elif message_who == 'tutor':
                message_body = request.data['message']
                subject = "Please respond within 2 days"

                sender = 'adminlessonpedia@gmail.com'
                recipient = 'andrewetedu@gmail.com' # client_email
                message = f"{message_body}\n\n{sender}"
                # print(message)

                send_mail(subject, message, sender, [recipient])
                return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Error sending email', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
