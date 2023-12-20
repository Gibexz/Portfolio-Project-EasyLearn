from django.urls import path
from . import views as general_views

urlpatterns = [
    path("", general_views.landing_page, name="landing_page"),
    path('tutor_sign_up/', general_views.tutor_sign_up, name='tutor_sign_up'),
    path('client_sign_up/', general_views.client_sign_up, name='client_sign_up'),
    path('app_admin_sign_up/', general_views.app_admin_sign_up, name='app_admin_sign_up'),
]
