from django.urls import path
from . import views as general_views

urlpatterns = [
    path("", general_views.landing_page, name="landing_page"),
    path("reviews/", general_views.reviews, name="reviews"),
    path("funTest/", general_views.fun_test, name="fun_test"),
    path("privacy/", general_views.privacy, name="privacy"),
    path("terms/", general_views.terms, name="terms"),
    path('tutor_sign_up/', general_views.tutor_sign_up, name='tutor_sign_up'),
    path('client_sign_up/', general_views.client_sign_up, name='client_sign_up'),
    path('app_admin_sign_up/', general_views.app_admin_sign_up, name='app_admin_sign_up'),
    # path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path("about_us/developers/", general_views.about_us, name="aboutUs"),


    path("api/get_tutors_reports/", general_views.get_tutors_reports, name="get_tutors_reports"),
    path("api/get_clients_reports/", general_views.get_clients_reports, name="get_clients_reports"),
]
