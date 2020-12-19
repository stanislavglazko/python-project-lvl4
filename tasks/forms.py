from django import forms
from .models import Task, TaskStatus


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name',
                  'description',
                  'status',
                  'creator',
                  'assigned_to',
                  'tags')


class TaskStatusForm(forms.ModelForm):

    class Meta:
        model = TaskStatus
        fields = ('name', )
