from django.shortcuts import render, redirect
from .forms import UserCreationForm, ClientRegistration
from django.http import HttpResponse

def clientRegister(request):
    """Post request with who am I concept"""
    if request.method == 'POST':
        form = ClientRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UserLogin')
        else:
            form = ClientRegistration()
            return render(request, 'register.html', {'form': form})
    else:
        form = ClientRegistration()
        return render(request, 'register.html', {'form': form})
