from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.user_register, name='user-register')
]