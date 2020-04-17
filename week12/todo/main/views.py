from django.shortcuts import render
from django.http import JsonResponse
from .models import TaskList as Tasklist
from .models import Task as Task
from .serializers import TaskListSerializer,TaskSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
#
# @csrf_exempt
# def task_list(request):
#     if request.method == 'GET':
#         task_lists = TaskList.objects.all()
#         serializer = TaskListSerializer(task_lists, many=True)
#         return JsonResponse(serializer.data, safe= False, status=200)
#     elif request.method == 'POST':
#         body = json.loads(request.body)
#         serializer = TaskListSerializer(data=body)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors)

class TaskListList(generics.ListCreateAPIView):

    queryset = Tasklist.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tasklist.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)


class TaskList(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def perform_create(self, serializer):
        serializer.save()

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

class TaskOfTaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            tasklist=Tasklist.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404

        queryset = tasklist.tasks.all()

        return queryset
