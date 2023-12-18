from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signed Up Successfully')
            return render(request, 'client/html/login.html')

        else:
            messages.error(request, 'Some Data Missing')

    else:
        form = UserRegisterForm()
        return render(request, 'client/html/register.html', {'form': form})