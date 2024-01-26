from django.urls import path
from .  import views


urlpatterns = [
    path('login/', views.tutor_login, name='tutor_login'),
    path('dashboard/', views.tutor_dashboard, name='tutor_dashboard'),
    path('logout/', views.tutor_logout, name='tutor_logout'),
    path('profile/', views.tutor_profile,name='tutor_profile' ),
    path('tutors/', views.view_tutors, name='view_tutors'),
    path('searchTutors/', views.search_tutors, name='search_tutors'),
    path('tutorDetail/<int:tutor_id>/', views.tutor_detail, name='tutor_detail'),
    path('emailTutor/<int:tutor_id>/', views.email_tutor, name='email_tutor'),
    path('quizGuide/', views.quiz_guide, name='quiz_guide'),
    path('quiz/', views.tutor_quiz, name='tutor_quiz'),
    path('adminSupport/', views.admin_support, name='admin_support'),
    path('suspendTutor/<int:tutor_id>/', views.suspend_tutor, name='suspend_tutor'),
    path('blockTutor/<int:tutor_id>/', views.block_tutor, name='block_tutor'),
    path('deleteSchedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
    path('uploadDocs/', views.upload_docs, name='upload_docs'),
    path('changePassword/', views.change_password, name='change_password'),
    path('moreUpdate/', views.more_update, name='more_update'),
    path('addSubject/', views.add_subject, name='add_subject'),
    path('updateSubject/<int:subject_id>/', views.update_subject, name='update_subject'),
    path('deleteSubject/<int:subject_id>/', views.delete_subject, name='delete_subject'),
    path('createContract/<int:tutor_id>/', views.create_contract, name='create_contract'),
    path('updateContractStatus/<contract_code>/', views.update_contract_status, name='update_contract_status'),
    path('terminate_contract', views.terminate_contract, name='terminate_contract'),
    path('reportAbuse/', views.report_abuse, name='report_abuse'),
    path('forgotPassword/', views.forgot_password, name='tutor_forgot_password'),
    path('ResetToken/', views.confirm_password_reset_token, name='tutor_reset_token'),
    path('resetPassword/', views.reset_password, name='tutor_reset_password'),
]