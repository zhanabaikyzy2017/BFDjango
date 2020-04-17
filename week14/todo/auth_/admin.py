from django.contrib import admin
from .models import MyUser,UserProfile

from django.contrib.auth.admin import UserAdmin


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username','email','is_staff')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','description','phone','city')
