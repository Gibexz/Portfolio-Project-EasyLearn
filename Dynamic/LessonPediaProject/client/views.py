from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .backends import EmailClientBackend as ClientBackend
from django.contrib import messages
from .form import UserProfileRegistrationForm
from .models import Client, Cart, Tutor, Ranking
from django.http import HttpResponse, JsonResponse
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
                    if user.deactivateByClient == 1:
                        login(request, user, backend='client.backends.EmailClientBackend')
                        next_param = request.POST.get('next', request.GET.get('next'))
                        if next_param:
                            return redirect(next_param)
                        else:
                            return redirect("landing_page")
                    else:
                        messages.error(request, "This account has been deactivated by User")
                else:
                    messages.error(request, "This account has been suspended by Admin")
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
        getAllTutors = Cart.objects.filter(client_id=request.user.id).all()
        countTutors = getAllTutors.count()
        return render(request, 'client/client_dashboard.html', {'tutors': getAllTutors, 'totalTutors': countTutors})
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
    activeUser.deactivateByClient = False
    activeUser.save()
    return redirect("logoutUser")

@login_required(login_url='client_signIn')
def profilePictureUpdate(request):
    """Update user profile picture"""
    activeUser = request.user
    if request.method == "POST":
        profilePicture = request.FILES.get('profilePicture')
        if profilePicture:
            get_previous_picture = activeUser.profile_picture
            if get_previous_picture:
                get_previous_picture.delete()
            activeUser.profile_picture = profilePicture
            activeUser.save()
            messages.success(request, "Profile Picture Succesfully Updated")
        else:
            messages.error(request, "No file was Uploaded")
        return redirect("validate_user", whoami=request.user)

@login_required(login_url='client_signIn')
def addTutor_2_cart(request, tutorId):
    """Add selected tutor to user Dashboard"""
    getThisTutor = get_object_or_404(Tutor, id=tutorId)
    inspectTutor = Cart.objects.filter(target_tutor=getThisTutor, client=request.user).all()
    for ids in inspectTutor:
        if ids.target_tutor.id == tutorId:
            messages.error(request, "Tutor already added to cart")
            return redirect('validate_user', whoami=request.user)
    obtained = Cart(
        target_tutor=getThisTutor,
        client = request.user,
    )
    obtained.save()
    messages.success(request, "Tutor successfully added to cart")
   
    return redirect('validate_user', whoami=request.user)

@login_required(login_url='client_signIn')
def removeTutorFromCart(request, tutorId):
    """Remove selected tutor from user Dashboard"""
    getTutor = Cart.objects.filter(target_tutor_id=tutorId, client=request.user).first()
    if getTutor:
        getTutor.delete()
        messages.success(request, "Tutor successfully removed from cart")
        return redirect('validate_user', whoami=request.user)
    messages.error(request, "Tutor not found in cart")
    return redirect('validate_user', whoami=request.user)

def tutors_ranking(request, tutorId, rankValue):
    """Rank tutor based on their performance and client satisfaction"""
    getTutor = get_object_or_404(Tutor, id=tutorId)
    queryRanks = Ranking.objects.filter(tutor=getTutor, client=request.user).first()
    if queryRanks:
        queryRanks.rank_number = rankValue
        #queryRanks.save()
        messages.success(request, "Ranking successfully updated")
        return redirect('validate_user', whoami=request.user)
    rank = Ranking(
        rank_number=rankValue,
        tutor=getTutor,
        client=request.user,
    )
    try:
        #rank.save()
        messages.success(request, "Ranking added successfully")
        return redirect('validate_user', whoami=request.user)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
