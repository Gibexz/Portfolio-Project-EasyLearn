from django.urls import path
from client import views

urlpatterns = [
    # path('register/', views.sign_up, name='signUp'),
    path('signIn/', views.client_login, name='client_signIn')
]