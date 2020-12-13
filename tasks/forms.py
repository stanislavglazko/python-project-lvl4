from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta(forms.ModelForm):
        model = Task
        fields = ('name',
                  'description',
                  'status',
                  'creator',
                  'assigned_to',
                  'tags')
