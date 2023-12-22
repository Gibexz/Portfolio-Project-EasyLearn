from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .backends import EmailClientBackend as ClientBackend
from django.contrib import messages
from .form import UserProfileRegistrationForm
from .models import Client
from django.http import HttpResponse
import re


#Check if input is email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def client_login(request):
    """client Login logic"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        if 'client' in request.path:
            check_pattern = is_valid_email(username)
            clientAuth = ClientBackend()
            if check_pattern:
                user = clientAuth.mail_authentication(request, username=username, password=password)
            else:
                user = clientAuth.username_authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user, backend='client.backends.EmailClientBackend')
                return render(request, 'client/login_landingpage.html', {'activeUser': user})
            else:
                messages.error(request, "Invalid User Credentials for client")
                return render(request, 'client/login.html')  
              
    return render(request, 'client/login.html')

def client_logout(request):
    """Logout active user"""
    logout(request)
    return redirect('landing_page')

def user_profile_registration(request):
    """Profile registration page"""
    current_user = request.user
    user_profile = Client.objects.get(username=current_user)
    if request.method == "POST":
        form = UserProfileRegistrationForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("validate_user", whoami=request.user)
        else:
            print(form.errors)
            return HttpResponse("Invalid form")
    else:
        form = UserProfileRegistrationForm()
        return render(request, 'client/profilePageUpdate.html', {"form": form, "activeUser": request.user})

def render_dashboard(request, whoami):
    """validate user and render dashboard
    or redirect user to register profile page"""

    user = Client.objects.get(username=whoami)
    address = user.residential_address
    
    if address:
        return render(request, 'client/client_dashboard.html')
    else:
        return redirect('user_profile')

