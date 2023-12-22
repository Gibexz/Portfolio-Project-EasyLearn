from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import AppAdmin
from client.models import Client
from tutor.models import Tutor


def app_admin_login(request):
    """Login view for admin"""
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        user = None
        if '@' in username_or_email:  # Check if the input is an email
            try:
                username1 = AppAdmin.objects.get(email=username_or_email)
                user = authenticate(username=username1, password=password)
                if user is not None and user.check_password(password):
                    login(request, user)
                    request.session['logged_in'] = True  # Set a session variable
                    request.session['account_type'] = 'admin'  # Set the user type in the session
                    return redirect('app_admin_dashboard')
                
            except AppAdmin.DoesNotExist:
                print('user does not exist or invalid credentials')
                pass
        else:
            user = authenticate(username=username_or_email, password=password)
        
        if user is not None and user.check_password(password):
            login(request, user)
            request.session['logged_in'] = True  # Set a session variable
            request.session['account_type'] = 'admin'  # Set the user type in the session
            return redirect('app_admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return redirect('app_admin_sign_up')



@login_required
def app_admin_dashboard(request):
    """"""
    account_type = 'admin'  # Assuming this is how you determine the account type
    return render(request, 'app_admin/admin_dashboard.html')



def app_admin_logout(request):
    """"""
    # Clear the session variable and log the user out
    if 'logged_in' in request.session:
        del request.session['logged_in']
    if 'account_type' in request.session:
        del request.session['account_type']
    
    logout(request)
    return redirect('app_admin_sign_up')


def get_tutor_count(request):
    """"""
    tutor_count = Tutor.objects.count()
    return JsonResponse({'tutor_count': tutor_count})