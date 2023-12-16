from django.shortcuts import render, HttpResponse
from tutors.forms import SignUpForm, UserCreationForm, SignUpTutor

# Create your views here.
def register(request):
    """tutors registration page"""
    form = SignUpForm(request.POST)
    return render(request, "register.html", {'form': form})

def signup(request, whoami):
    """test page"""
    if whoami == 'learner':
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                email = form.cleaned_data.get("email")
                form.save()
                return HttpResponse("hello")
            else:
                print(form.errors)
                return HttpResponse(form.errors)
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})
    
    
def SignUpTutor(request, whoami):
    """render template for tutor"""
    if whoami == 'tutor':
        if request.method == 'POST':
            form = SignUpTutor(request.POST)
            if form.is_valid():
                pass
    return HttpResponse("hello")
