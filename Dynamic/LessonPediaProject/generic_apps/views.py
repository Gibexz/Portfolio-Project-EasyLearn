from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientRegisterForm, TutorRegisterForm, AppAdminRegisterForm
from app_admin.models import AppAdmin
from tutor.models import Tutor
from client.models import Client
from django.contrib.auth.models import AnonymousUser
from .serializers import ClientReportAbuseSerializer, TutorReportAbuseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ClientReportAbuse, TutorReportAbuse
from django.contrib.auth.decorators import login_required


def landing_page(request):
    """Landing page"""
    active_user = request.user
    if isinstance(active_user, AnonymousUser):
        print(active_user)
        return render(request, "generic_apps/landingpage.html")
    
    else:
        model_name = active_user._meta.model_name
        if isinstance(request.user, Tutor):
            return render(request, "generic_apps/login_landingpage.html", {"activeUser":request.user, 'model': model_name})
        elif isinstance(request.user, Client):
            return render(request, "generic_apps/login_landingpage.html", {"activeUser":request.user, 'model': model_name})
    return render(request, "generic_apps/landingpage.html")


def client_sign_up(request):
    """sign_up for client"""
    if request.method == 'POST':
       form = ClientRegisterForm(request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Registration Successful! Please Login')
        #    return redirect('user_login')
           return redirect('client_signIn')
       if form.errors:
                # Access and display first error for each field
           for field, errors in form.errors.items():
               messages.error(request, f"{field.title()}: {errors[0]}")
               return render(request, 'generic_apps/client_sign_up.html')
       else:
                # Handle non-field errors if any
           for error in form.non_field_errors:
               messages.error(request, error)
               context = {'form': form}
               return render(request, 'generic_apps/client_sign_up.html', context=context)

    else:
        form = ClientRegisterForm()
        context = {'form': form}
        return render(request, 'generic_apps/client_sign_up.html', context=context)
    

def tutor_sign_up(request):
    """sign_up for tutors"""
    if request.method == 'POST':
       form = TutorRegisterForm(request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Registration Successful! Please Login')
           return redirect('tutor_login')
       else:
            messages.error(request, 'Please correct the error below.')
            form = TutorRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/tutor_sign_up.html', context=context)

    else:
            form = TutorRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/tutor_sign_up.html', context=context)


def app_admin_sign_up(request):
    """sign_up for admin"""
    if request.method == 'POST':
        form = AppAdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful! Please Login')
            return redirect('app_admin_sign_up')
        
        else:
            messages.error(request, 'Please correct the error below.')
            form = AppAdminRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/app_admin_sign_up.html', context=context)
    else:
        form = AppAdminRegisterForm()
        context = {'form': form}
        return render(request, 'generic_apps/app_admin_sign_up.html', context=context)



# Tutors report abuse logics for appAdmin
@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_tutors_reports(request):
    """ get tutor reports data api using django rest framwork"""
    if request.method == 'GET':
        tutors_reports = TutorReportAbuse.objects.all().order_by('-created_at')
        
        tutors_reports_serialized = TutorReportAbuseSerializer(tutors_reports, many=True)
        
        return Response({
            'tutors_reports': tutors_reports_serialized.data  # Serialized tutor data
        }, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

# Clients report abuse logics for appAdmin
@api_view(['GET'])
@login_required(login_url='app_admin_sign_up')
def get_clients_reports(request):
    """ get client reports data api using django rest framwork"""
    if request.method == 'GET':
        clients_reports = ClientReportAbuse.objects.all().order_by('-created_at')
        
        clients_reports_serialized = ClientReportAbuseSerializer(clients_reports, many=True)
        
        return Response({
            'clients_reports': clients_reports_serialized.data  # Serialized tutor data
        }, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
