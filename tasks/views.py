from django.shortcuts import render  # noqa: F401
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, TaskStatus
from .forms import TaskForm, TaskStatusForm
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


class NewStatus(LoginRequiredMixin, CreateView):
    model = TaskStatus
    template_name = 'tasks/new_status.html'
    form_class = TaskStatusForm
    success_url = reverse_lazy('statuses')


class ListOfStatuses(LoginRequiredMixin, ListView):
    model = TaskStatus
    template_name = 'tasks/statuses.html'
    context_object_name = 'statuses'


class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = TaskStatus
    template_name = 'tasks/update_status.html'
    success_url = reverse_lazy('statuses')
    form_class = TaskStatusForm


class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = TaskStatus
    template_name = 'tasks/delete_status.html'
    success_url = reverse_lazy('statuses')
