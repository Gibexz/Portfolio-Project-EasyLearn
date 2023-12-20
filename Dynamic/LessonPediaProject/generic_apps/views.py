from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientRegisterForm, TutorRegisterForm, AppAdminRegisterForm


def landing_page(request):
    """Landing page"""
    return render(request, "generic_apps/landingpage.html")


def client_sign_up(request):
    """sign_up for client"""
    if request.method == 'POST':
       form = ClientRegisterForm(request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Registration Successful!')
        #    return redirect('user_login')
           return redirect('landing_page')
       if form.errors:
                # Access and display first error for each field
           for field, errors in form.errors.items():
               messages.error(request, f"{field.title()}: {errors[0]}")
       else:
                # Handle non-field errors if any
           for error in form.non_field_errors:
               messages.error(request, error)
               context = {'form': form}
               return render(request, 'generic_apps/sign_up.html', context=context)

    else:
        form = ClientRegisterForm()
        context = {'form': form}
        return render(request, 'generic_apps/sign_up.html', context=context)
    

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
            form = ClientRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/sign_up.html', context=context)

    else:
            form = ClientRegisterForm()
            context = {'form': form}
            return render(request, 'generic_apps/sign_up.html', context=context)


def app_admin_sign_up(request):
    """sign_up for admin"""
    if request.method == 'POST':
       form = AppAdminRegisterForm(request.POST) 
       if form.is_valid():
           form.save()
           messages.success(request, 'Registration Successful!')
           return redirect('user_login')
       else:
            messages.error(request, 'Please correct the error below.')
            return redirect('landing_page')

    else:
        form = AppAdminRegisterForm()
        context = {'form': form}
        return render(request, 'app_admin_sign_up', context=context)
