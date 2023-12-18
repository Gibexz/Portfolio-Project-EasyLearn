from django.shortcuts import render

# Create your views here.
def landing_page(request):
    """Landing page"""
    return render(request, "app_admin/landingpage.html")
