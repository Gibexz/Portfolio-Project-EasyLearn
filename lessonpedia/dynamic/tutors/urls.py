from django.urls import path
from . import views

urlpatterns = [
    path('signup/<str:whoami>/', views.signup, name='signup'),
    path('signup/', views.register, name="no_args")
]