from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_.models import MyUser

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username','email','is_staff')

