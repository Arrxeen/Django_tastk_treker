from django.urls import path
from . import views
urlpatterns = [
    path('', views.TaskListViews.as_view(), name='task-list'),
    path('<int:pk>', views.TaskDetailViews.as_view(), name='task-detail'),
    path('created/',views.TaskCratedViews.as_view(), name='task-created')
]
