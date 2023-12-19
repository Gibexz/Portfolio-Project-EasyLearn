from django.shortcuts import render
from django.contrib.auth import authenticate, login
import re

# Create your views here.
def mail_validation(text):
    """Check if the text is email"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.search(email_pattern, text) is not None

def user_login(request):
    """Login for all users"""
    if  request.method == 'POST':
        username_or_email = request.POST["useremail"]
        password = request.POST["password"]
        
        check = mail_validation(username_or_email)
        if check:
            user = authenticate(request, email=username_or_email, password=password)
            print(user)
        else:
            user = authenticate(request, username=username_or_email, password=password)
            print(user)

    return render(request, 'login.html')
