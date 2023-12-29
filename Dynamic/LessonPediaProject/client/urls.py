from django.urls import path
from client import views

urlpatterns = [
    # path('register/', views.sign_up, name='signUp'),
    path('signIn/', views.client_login, name='client_signIn'),
    path('User_logout', views.client_logout, name="logoutUser"),
    path('signIn/User_dashboard/<str:whoami>', views.render_dashboard, name='validate_user'),
    path('signIn/User_Profile_Registration/', views.user_profile_registration, name='user_profile'),
    path('SignIn/User_dashboard/ProfileUpdate', views.ClientProfileUpdate, name='ProfileUpdate'),
    path('SignIn/User_dashboard/Password_change', views.ClientChangePassword, name='changePassword'),
    path("user/deactivate", views.deactivate_account, name="remove_user"),
]