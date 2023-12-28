from django.urls import path
from .  import views


urlpatterns = [
    path('login/', views.tutor_login, name='tutor_login'),
    path('dashboard/<tutor>', views.tutor_dashboard, name='tutor_dashboard'),
    path('logout/', views.tutor_logout, name='tutor_logout'),
    path('profile/', views.tutor_profile,name='tutor_profile'),
    path('tutor-view_page', views.tutor_view_page, name='tutor_view_page')
]