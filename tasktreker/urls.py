from django.urls import path
from . import views
urlpatterns = [
    path('', views.TaskListViews.as_view(), name='task-list'),
    path('<int:pk>', views.TaskDetailViews.as_view(), name='task-detail'),
    path('created/', views.TaskCreateView.as_view(), name='task-created'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('comment/like/<int:pk>/',views.CommentLikeToggel.as_view(), name="comment-toggle-like")
]
