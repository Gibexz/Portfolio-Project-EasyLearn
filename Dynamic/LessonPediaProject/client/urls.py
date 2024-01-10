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
    path("user/profile_picture_Update", views.profilePictureUpdate, name="dpUpdate"),
    path("user/add_tutor/<int:tutorId>", views.addTutor_2_cart, name='add_tutor'),
    path("user/remove_tutor/<int:tutorId>", views.removeTutorFromCart, name='remove_tutor'),
    path("tutor/ranking/<int:tutorId>/<int:rankValue>", views.tutors_ranking, name='rank_tutor'),
    path("filter/tutor/keyword=/<str:keyword>", views.search_algorithm, name="filter_keyword"),
    path("review/tutorid/<int:tutorId>", views.review_tutor_ajax, name="reviewTutor"),
    path("review/tutor/submit/<int:tutorId>", views.submit_review, name='submitReview'),
    path("review/tutor/editReview/<int:tutorId>", views.edit_review, name='editReview'),
    path("api/contractForm", views.contract_information, name="contractInfo"),
    path("payment/paystackGateway/<int:tutorId>", views.paystackGateway, name="makePayment"),
    path("transaction/details/<int:tutorId>", views.transactionDetails_storage, name="transactionDetails"),
    path("api/contract/information", views.transaction_information, name="transactionInfo"),
]