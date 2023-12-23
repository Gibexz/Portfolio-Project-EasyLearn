from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientRegisterForm, TutorRegisterForm, AppAdminRegisterForm
from django.contrib.auth.models import AnonymousUser
from client.models import Client

def landing_page(request):
    """Landing page"""
    active_user = request.user
    if isinstance(active_user, AnonymousUser):
        return render(request, "generic_apps/landingpage.html")
    else:
        checkActiveUser = (isinstance(request.user, Client))
        if checkActiveUser:
            return render(request, "client/login_landingpage.html", {"activeUser":request.user})

def client_sign_up(request):
    """sign_up for client"""
    if request.method == 'POST':
       form = ClientRegisterForm(request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Registration Successful, please Login!')
        #    return redirect('user_login')
           return redirect('client_signIn')
       if form.errors:
                # Access and display first error for each field
           for field, errors in form.errors.items():
               form = ClientRegisterForm()
               messages.error(request, f"{field.title()}: {errors[0]}")
               return render(request, 'generic_apps/client_sign_up.html', {'form': form})
       else:
                # Handle non-field errors if any
           for error in form.non_field_errors:
               messages.error(request, error)
               form = ClientRegisterForm()
               context = {'form': form}
               return render(request, 'generic_apps/client_sign_up.html', context=context)

    else:
        form = ClientRegisterForm()
        context = {'form': form}
        return render(request, 'generic_apps/client_sign_up.html', context=context)
    

def tutor_sign_up(request):
    """sign_up for tutors"""
    if request.method == 'POST':
       form = TutorRegisterForm(request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Registration Successful!')
           return redirect('landing_page')
       else:
            messages.error(request, 'Please correct the error below.')
            form = TutorRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/tutor_sign_up.html', context=context)

    else:
            form = TutorRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/tutor_sign_up.html', context=context)


def app_admin_sign_up(request):
    """sign_up for admin"""
    if request.method == 'POST':
        form = AppAdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful!')
            return redirect('app_admin_sign_up')
        
        else:
            messages.error(request, 'Please correct the error below.')
            form = AppAdminRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/app_admin_sign_up.html', context=context)
    else:
        form = AppAdminRegisterForm()
        context = {'form': form}
        return render(request, 'generic_apps/app_admin_sign_up.html', context=context)