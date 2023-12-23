from django.urls import path
from .  import views


urlpatterns = [
    path('login/', views.tutor_login, name='tutor_login'),
    path('dashboard/<int:tutor_id>/', views.tutor_dashboard, name='tutor_dashboard'),
]