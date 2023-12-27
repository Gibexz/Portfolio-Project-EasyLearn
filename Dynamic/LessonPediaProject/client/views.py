from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .backends import EmailClientBackend as ClientBackend
from django.contrib import messages
from .form import UserProfileRegistrationForm
from .models import Client
from django.http import HttpResponse
import re

def logout_required(view_func):
    """Decorator to require the user to be logged out to access a view."""
    def _wrapped_view(request):
        if request.user.is_authenticated and "client" in request.path:
            messages.error(request, f"{request.user} is already Signed in, please Sign Out!")
            return redirect('landing_page') 
        return view_func(request) 
    return _wrapped_view

@logout_required
def client_login(request):
    """client Login logic"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if 'client' in request.path:
            clientAuth = ClientBackend()
            user = clientAuth.authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active == 1:
                    login(request, user, backend='client.backends.EmailClientBackend')
                    next_param = request.POST.get('next', request.GET.get('next'))
                    if next_param:
                        return redirect(next_param)
                    else:
                        return redirect("landing_page")
                else:
                    messages.error(request, "This account has been deactivated by User")
            else:
                messages.error(request, "Invalid User Credentials for client")
                return render(request, 'client/login.html') 
              
    return render(request, 'client/login.html')

@login_required(login_url='client_signIn')
def client_logout(request):
    """Logout active user"""
    logout(request)
    return redirect('landing_page')

@login_required(login_url='client_signIn')
def user_profile_registration(request):
    """Profile registration page"""
    current_user = request.user
    user_profile = Client.objects.get(username=current_user)
    if request.method == "POST":
        form = UserProfileRegistrationForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("validate_user", whoami=request.user)
        else:
            return HttpResponse("Invalid form")
    else:
        form = UserProfileRegistrationForm()
        return render(request, 'client/profilePageUpdate.html', {"form": form, "activeUser": request.user})

@login_required(login_url='client_signIn')
def render_dashboard(request, whoami):
    """validate user and render dashboard
    or redirect user to register profile page"""

    user = Client.objects.get(username=whoami)
    address = user.residential_address
    
    if address:
        return render(request, 'client/client_dashboard.html')
    else:
        return redirect('user_profile')

@login_required(login_url='/landing_page/')
def ClientProfileUpdate(request):
    """User profile update from dashboard"""
    activeUser = request.user
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phoneNumbs = request.POST.get('phoneNumber')
        residentAddress = request.POST.get('address')
        state_Residence = request.POST.get('state')
        national = request.POST.get('nationality')
        if firstName:
            activeUser.first_name = firstName
        if lastName:
            activeUser.last_name = lastName
        if phoneNumbs:
            activeUser.phone_number = phoneNumbs
        if residentAddress:
            activeUser.residential_address = state_Residence
        if national:
            activeUser.nationality = national
        if firstName or lastName or phoneNumbs or residentAddress or national:
            messages.success(request, "User Profile Succesfully Updated")
            activeUser.save()
        else:
            messages.error(request, "No field was Updated")
        return redirect("validate_user", whoami=request.user)

@login_required(login_url='/landing_page/')
def ClientChangePassword(request):
    """Change User Password"""
    activeUser = request.user
    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new_password = request.POST.get('newPassword')
        confirm_new_password = request.POST.get('confirmNewPassword')
        form = PasswordChangeForm(activeUser, {'old_password': old_password, 'new_password1': new_password, 'new_password2': confirm_new_password})
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Successfully Updated")
            return redirect("validate_user", whoami=request.user)
        elif form.errors:
            try:
                for field, errors in form.errors.items():
                    form = PasswordChangeForm(activeUser)
                    messages.error(request, f"{field.title()}: {errors[0]}")
                    #break
                    return render(request, 'client/client_dashboard.html')
            except Exception:
                return HttpResponse("An error occurred. Please try again later.")
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'client/client_dashboard.html')

@login_required(login_url='/landing_page/')
def deactivate_account(request):
    """deactivate account as requested by user"""
    activeUser = request.user
    activeUser.is_active = False
    activeUser.save()
    return redirect("logoutUser")