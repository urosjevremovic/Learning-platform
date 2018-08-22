from django.urls import path

from user.views import UserRegistrationView, UserEnrollCourseView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('enroll-course/', UserEnrollCourseView.as_view(), name='user_enroll_course'),
]