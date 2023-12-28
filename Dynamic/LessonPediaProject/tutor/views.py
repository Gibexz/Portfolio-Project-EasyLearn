from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .backends import TutorAuthBackend
from .profile_update_form import TutorUpdateForm
from .models import Tutor





# @login_required(login_url='tutor_login')
def tutor_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        tutor = TutorAuthBackend().authenticate(request, username_or_email=username_or_email, password=password)
        if tutor:
            if 'tutor' in request.path:
                login(request, tutor, backend='tutor.backends.TutorAuthBackend')
                messages.success(request, "You're Logged In")
                if tutor.certificate:
                    return redirect('tutor_dashboard', tutor=tutor)
                return redirect ('tutor_profile')

        else:
            tutor_exists = Tutor.objects.filter(username=username_or_email).exists()
            if tutor_exists:
                messages.error(request, 'Incorrect Password')
            else:
                messages.error(request, 'User Not Found')

            return render(request, 'tutor/tutor_login.html', context={'username_or_email': username_or_email})

    else:
        return render(request, 'tutor/tutor_login.html')
    
    
@login_required(login_url='tutor_login')
def tutor_dashboard(request, tutor):
    """Displays Tutor Dashboard"""
    tutor = get_object_or_404(Tutor, username=tutor)
    return render(request, 'tutor/tutor_dashboard.html', context={'tutor': tutor})

@login_required(login_url='tutor_login')
def tutor_profile(request):
    """profile update form"""
    tutor = Tutor.objects.filter(username=request.user.username).first()

    if tutor is not None:
        if request.method == 'POST':
            form = TutorUpdateForm(request.POST, request.FILES, instance=tutor)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successfully')
                return redirect('tutor_dashboard', tutor_id=tutor.id)
            else:
                messages.error(request, 'Profile Update Failed')
                return render(request, 'tutor/tutor_profile.html', context={'form': form, 'tutor': tutor})
        else:
            form = TutorUpdateForm(instance=tutor)
            return render(request, 'tutor/tutor_profile.html', context={'form': form, 'tutor': tutor, 'form_errors': form.errors})
    
    else:
        messages.error(request, 'Tutor not found for the given username')
        return redirect('tutor_login')
    
def tutor_logout(request):
    logout(request)
    messages.success(request, "You're Logged Out")
    return redirect('tutor_login')

def tutor_view_page(request):
    """Rewrite this to the way that will suit you"""
    return render(request, 'tutor/tutorView.html')