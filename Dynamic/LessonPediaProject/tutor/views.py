from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .tutor_backends import TutorAuthBackend
from .models import Tutor
from django.contrib.auth.decorators import login_required


def tutor_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        # print('Incoming request:', username_or_email, password)
        tutor = TutorAuthBackend().authenticate(request, username_or_email=username_or_email, password=password)
        # print('Tutor:', tutor)
        if tutor:
            login(request, tutor, backend='tutor.backends.TutorAuthBackend')
            messages.success(request, "You're Logged In")
            return redirect('tutor_dashboard',  tutor_id=tutor.id)

        else:
            tutor_exists = Tutor.objects.filter(username=username_or_email).exists()
            if tutor_exists:
                messages.error(request, 'Incorrect Password')
            else:
                messages.error(request, 'User Not Found')

            return render(request, 'tutor/tutor_login.html', context={'username_or_email': username_or_email})

    else:
        return render(request, 'tutor/tutor_login.html')
    

def tutor_dashboard(request, tutor_id):
    """Displays Tutor Dashboard"""
    print(request.user.is_authenticated)
    tutor = get_object_or_404(Tutor, id=tutor_id)
    return render(request, 'tutor/tutor_dashboard.html', context={'tutor': tutor})