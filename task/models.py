from django.db import models
from category.models import TaskCategory
# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=255)
    taskDescription = models.TextField()
    categories = models.ManyToManyField(TaskCategory, related_name='tasks')
    task_assign_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.taskTitle