from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView
from .forms import TaskForm
from django.urls import reverse_lazy

class TaskListViews(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetailViews(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCratedViews(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')