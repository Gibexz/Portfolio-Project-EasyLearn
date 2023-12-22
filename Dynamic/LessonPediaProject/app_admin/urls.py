from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.app_admin_dashboard, name="app_admin_dashboard"),
    path("login/", views.app_admin_login, name="app_admin_login"),
    path("logout/", views.app_admin_logout, name="app_admin_logout"),
    path("api/get_tutor_count/", views.get_tutor_count, name="get_tutor_count"),
]