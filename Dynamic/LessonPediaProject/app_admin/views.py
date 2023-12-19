from django.shortcuts import render

# Create your views here.
def landing_page(request):
    """Landing page"""
    return render(request, "landingpage.html")

def register(request):
    """Register User and client"""
    return render(request, 'register.html')