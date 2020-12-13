from django.shortcuts import render  # noqa: F401
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
# Create your views here.


class ListOfTasks(ListView):
    model = Task
    template_name = 'tasks/tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_tasks'] = Task.objects.all()
        return context


class NewTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/new_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
