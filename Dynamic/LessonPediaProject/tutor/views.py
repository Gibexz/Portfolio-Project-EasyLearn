from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from .tutor_backends import TutorAuthBackend
from .profile_update_form import TutorUpdateForm
from .models import Tutor
from django.contrib.auth.decorators import login_required


def tutor_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        tutor = TutorAuthBackend().authenticate(request, username_or_email=username_or_email, password=password)
        if tutor:
            login(request, tutor, backend='tutor.backends.TutorAuthBackend')
            messages.success(request, "You're Logged In")
            if tutor.profile_picture:
                print("Profile Picture:", tutor.profile_picture.url)
                return redirect('tutor_dashboard', tutor_id=tutor.id)
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
    
# def tutor_dashboard(request, tutor_id):
#     if request.user.is_authenticated:
#         print("User is authenticated:", request.user)
#         print("Session ID:", request.session.session_key)
#         print("CSRF Token:", request.COOKIES.get("csrftoken"))
#         print("Request:", request)
#         return render(request, 'tutor/tutor_dashboard.html', context={'tutor_id': tutor_id})
#     else:
#         print("User not authenticated. Redirecting to login.")
#         return redirect('tutor_login')
    
def tutor_dashboard(request, tutor_id):
    """Displays Tutor Dashboard"""
    # print(request.user.is_authenticated)
    # print(request)
    # print(request.user)
    # print(request.user.username)
    # print(request.session.session_key)
    # if not request.user.is_authenticated:
    #     print("User not authenticated. Redirecting to login.")
    #     return redirect('tutor_login')
    tutor = get_object_or_404(Tutor, id=tutor_id)
    return render(request, 'tutor/tutor_dashboard.html', context={'tutor_id': tutor.id})

def tutor_profile(request):
    """profile update form"""
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        print("User not authenticated. Redirecting to login.")
        return redirect('tutor_login')
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
    
@login_required
def tutor_logout(request):
    logout(request)
    messages.success(request, "You're Logged Out")
    return redirect('tutor_login') 