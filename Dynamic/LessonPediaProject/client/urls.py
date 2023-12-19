from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.register, name='default'),
    path('sign_up/<str:whoami>', views.register, name="clientSignUp")
]