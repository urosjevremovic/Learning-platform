from django.urls import path

from user.views import UserRegistrationView

app_name = 'users'
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
]