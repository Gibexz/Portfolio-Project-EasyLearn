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
    path('emailTutor/<int:tutor_id>/', views.email_tutor, name='email_tutor'),
    path('quizGuide/', views.quiz_guide, name='quiz_guide'),
    path('quiz/', views.tutor_quiz, name='tutor_quiz'),
    path('adminSupport/', views.admin_support, name='admin_support'),
    path('suspendTutor/<int:tutor_id>/', views.suspend_tutor, name='suspend_tutor'),
    path('blockTutor/<int:tutor_id>/', views.block_tutor, name='block_tutor'),
]