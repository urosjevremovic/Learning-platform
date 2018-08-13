from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'password', 'date_of_birth', 'photo', 'email', 'bio']
