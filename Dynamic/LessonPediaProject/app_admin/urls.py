from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.app_admin_dashboard, name="app_admin_dashboard"),
    path("login/", views.app_admin_login, name="app_admin_login"),
    path("logout/", views.app_admin_logout, name="app_admin_logout"),

    ##Tutor APIs##
    path("api/get_admin_username/", views.get_admin_username, name='get_admin_username'),
    path("api/get_tutors_data/", views.get_tutors_data, name="get_tutors_data"),
    path("api/get_tutor_count/", views.get_tutor_count, name="get_tutor_count"),
    path("api/get_nos_active_tutors/", views.get_nos_active_tutors, name="get_nos_active_tutors"),
    path("api/get_nos_inactive_tutors/", views.get_nos_inactive_tutors, name="get_nos_inactive_tutors"),


    ##Clients APIs##
    path("api/get_clients_data/", views.get_clients_data, name="get_clients_data"),
    path("api/get_client_count/", views.get_client_count, name="get_client_count"),
    path("api/get_nos_active_clients/", views.get_nos_active_clients, name="get_nos_active_clients"),
    path("api/get_nos_inactive_clients/", views.get_nos_inactive_clients, name="get_nos_inactive_clients"),
    
]