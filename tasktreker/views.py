from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task, Comment, Like
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from .forms import TaskForm, TaskFilterForm , CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixin import UserIsOwnerMixin

class TaskListViews(ListView):
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status','')
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailViews(DetailView):
    model = Task
    context_object_name = 'task'
    
    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coment_form"] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        coment_form = CommentForm(request.POST, request.FILES)
        if coment_form.is_valid():
            comment = coment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('task-detail', pk=comment.task.pk)
    

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin,UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class CommentLikeToggel(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=self.kwargs.get("pk"))
        likeq = Like.objects.filter(comment = comment, user = request.user)
        if likeq.exists():
            likeq.delete()
        else:
            Like.objects.create(comment = comment, user = request.user)
        return HttpResponseRedirect(comment.get_absolute_url())
    

class CustomLoginView(LoginView):
    template_name = 'tasktreker/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = 'login'


class RegisterView(CreateView):
    template_name = 'tasktreker/register.html'
    form_class = UserCreationForm
    
    def form_valid(self, form): 
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy('login'))