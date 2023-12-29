from django.urls import path
from .  import views


urlpatterns = [
    path('login/', views.tutor_login, name='tutor_login'),
    path('dashboard/', views.tutor_dashboard, name='tutor_dashboard'),
    path('logout/', views.tutor_logout, name='tutor_logout'),
    path('profile/', views.tutor_profile,name='tutor_profile' ),
    path('tutors/', views.view_tutors, name='view_tutors'),
    path('searchTutors/', views.search_tutors, name='search_tutors'),
    path('submitRank/<int:tutor_id>/', views.submit_rank, name='submit_rank'),
    path('tutorDetail/<int:tutor_id>/', views.tutor_detail, name='tutor_detail'),
]