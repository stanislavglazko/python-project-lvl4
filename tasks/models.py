from django.db import models
from users.models import CustomUser
from taggit.managers import TaggableManager
# Create your models here.


class TaskStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=10000)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE,
                               related_name='status')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                related_name='creator')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                    related_name='assigned_to')
    tags = TaggableManager()

    def __str__(self):
        return self.name
