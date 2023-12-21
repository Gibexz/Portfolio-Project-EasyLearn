from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .backends import EmailClientBackend as ClientBackend
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
                return redirect('landing_page')
              
    return render(request, 'client/login.html')

