from django.urls import path, include
from . import views

app_name = 'views'

urlpatterns = [
    path("", views.home, name='home')
]