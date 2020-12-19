from django import forms
from .models import Task, TaskStatus, Tag


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


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name', )
