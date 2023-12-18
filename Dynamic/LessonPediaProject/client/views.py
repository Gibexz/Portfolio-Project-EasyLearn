from django.shortcuts import render, redirect

from .form import ClientSignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'client/login.html')
        else:
            # Form is not valid, render the registration template with errors
            context = {'form': form}
            return render(request, 'client/register.html', context=context)
        
    else:
        form = ClientSignUpForm()
        context = {'form': form}

        return render(request, 'client/register.html', context=context)
            


