from django.urls import path
from .views import TaskListList,TaskListDetail,TaskList, TaskDetail, TaskOfTaskList


urlpatterns=[
    path('task_lists/',TaskListList.as_view()),
    path('task_lists/<int:pk>/',TaskListDetail.as_view() ),
    path('tasks/',TaskList.as_view()),
    path('tasks/<int:pk>/',TaskDetail.as_view()),
    path('task_list/<int:pk>/tasks/', TaskOfTaskList.as_view()),

]