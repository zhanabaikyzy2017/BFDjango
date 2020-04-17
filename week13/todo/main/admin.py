from django.contrib import admin
from .models import TaskList,Task

@admin.register(TaskList)
class TaskListAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'due_date','status','created_by')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','list_id','status')
