from django.shortcuts import render
from .models import Client
from .forms import UserCreationForm, ClientRegistration
from django.http import HttpResponse

def register(request, whoami):
    """Post request with who am I concept"""
    if request == 'POST' and whoami == 'learner':
        form = ClientRegistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html")
        else:
            return HttpResponse("there's an error")
    else:
        form = ClientRegistration()
        return request(request, 'register.html', {'form': "hello"})
