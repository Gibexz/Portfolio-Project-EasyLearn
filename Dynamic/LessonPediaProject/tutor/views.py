from django.shortcuts import render
from .form import TutorRegistration
from django import forms
from django.contrib import messages

def tutorRegister(request):
    """Get tutors registered to its database"""
    if request.method == 'POST':
        form = TutorRegistration(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
        else:
            messages.error(request, "form.errors")
            return render(request, 'tutor_register.html', {'form': form})
    else:
        form = TutorRegistration()
        return render(request, 'tutor_register.html', {'form': form})