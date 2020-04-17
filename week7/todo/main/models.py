from django.db import models
from auth_.models import MyUser

class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(auto_now_add = False)
    status = models.CharField(max_length = 200)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=1)
    objects = TaskListManager()

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = "Tasklists"

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.name, self.created_at, self.due_date, self.status)

class TaskManager(models.Manager):
    pass

class Task(models.Model):
    STATUSES=(
        (1,'new'),
        (2,'in progress'),
        (3,'done')
    )
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    list = models.ForeignKey(TaskList, on_delete=models.CASCADE,related_name='tasks')
    status = models.IntegerField(choices=STATUSES)
    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural="Tasks"

