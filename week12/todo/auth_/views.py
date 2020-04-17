from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from auth_.models import MyUser
from auth_.serializer import MyUserSerializer
import logging


class MyUserAPIView(generics.CreateAPIView):
    permission_classes =(AllowAny,)
    serializer_class = MyUserSerializer


    def get_queryset(self):
        return MyUser.objects.all()

    def perform_create(self,serializer):
        username =self.request.data.pop('username')
        password =self.request.data.pop('password')
        # email = self.request.data.pop('email')

        user,created=MyUser.objects.get_or_create(username=username)
        user.set_password(password)
        # user.set_email(email)
        user.save()

