from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task, TaskStatus, Tag
from .forms import TaskForm, TaskStatusForm, TagForm
from .filters import TaskFilter
# Create your views here.


class NewTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/new_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy('tasks')
    form_class = TaskForm


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
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


def tasklist(request):
    f = TaskFilter(request.GET, queryset=Task.objects.all())
    return render(request, 'tasks/tasks.html', {'filter': f})


class NewTag(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = 'tasks/new_tag.html'
    form_class = TagForm
    success_url = reverse_lazy('new_task')
