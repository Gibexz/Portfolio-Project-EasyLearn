from django.shortcuts import render

# Create your views here.
def landing_page(request):
    """Landing page"""
    return render(request, "landingpage.html")
