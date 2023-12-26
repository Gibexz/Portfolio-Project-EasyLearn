from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import AppAdmin
from client.models import Client
from tutor.models import Tutor
from .backends import AppAdminAuthBackend
from .serializers import ClientSerializer, TutorSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import hashlib


def generate_browser_fingerprint(request):
    """Generate a unique fingerprint based on browser information"""
    user_agent = request.META.get('HTTP_USER_AGENT', '').encode()
    ip_address = request.META.get('REMOTE_ADDR', '').encode()

    fingerprint = hashlib.sha256((user_agent + ip_address)).hexdigest()
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

        is_email = False
        if '@' in username_or_email:  # Check if the input is an email
            try:
                validate_email(username_or_email)
                is_email = True
            except ValidationError:
                is_email = False
        
        AppAdminAuth = AppAdminAuthBackend()
        if is_email:
            user = AppAdminAuth.email_aunthentication(request, username=username_or_email, password=password)
        else:
            user = AppAdminAuth.username_aunthentication(request, username=username_or_email, password=password)
        
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

        # show_all_tutors = request.GET.get('all_tutors')
        # if show_all_tutors:
        #     return render(request, 'app_admin/admin_dashboard.html', {'tutors': all_tutors, 'clients': all_clients, 'show_tutor_pagination': True})
        
        # show_all_clients = request.GET.get('all_clients')
        # if show_all_clients:
        #     return render(request, 'app_admin/admin_dashboard.html', {'tutors': all_tutors, 'clients': all_clients, 'show_client_pagination': True})

        # Pagination for tutors
        # paginator_tutor = Paginator(all_tutors, 3)  # Show 3 tutors per page
        # page_number_tutor = request.GET.get('page_tutors')

        # try:
        #     tutors = paginator_tutor.page(page_number_tutor)
        # except PageNotAnInteger:
        #     # If page is not an integer, deliver first page
        #     tutors = paginator_tutor.page(1)
        # except EmptyPage:
        #     # If page is out of range, deliver last page of results
        #     tutors = paginator_tutor.page(paginator_tutor.num_pages)

        # Pagination for clients
        # paginator_client = Paginator(all_clients, 3)
        # page_number_client = request.GET.get('page_clients')

        # try:
        #     clients = paginator_client.page(page_number_client)
        # except PageNotAnInteger:
        #     clients = paginator_client.page(1)
        # except EmptyPage:
        #     clients = paginator_client.page(paginator_client.num_pages)

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
            'tutors_data': clients_data_serialized.data  # Serialized tutor data
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