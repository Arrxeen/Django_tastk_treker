from django.urls import path
from . import views
urlpatterns = [
    path('', views.TaskListViews.as_view(), name='task-list'),
    path('<int:pk>', views.TaskDetailViews.as_view(), name='task-detail'),
    path('created/', views.TaskCreateView.as_view(), name='task-created'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('comment/like/<int:pk>/',views.CommentLikeToggel.as_view(), name="comment-toggle-like"),
    path('comment/dislike/<int:pk>/', views.CommentDislikeToggel.as_view(), name="comment-toggle-dislike"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('delete/<int:pk>', views.TaskDeliteView.as_view(), name='task-delete')
]
