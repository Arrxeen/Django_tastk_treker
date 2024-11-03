from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Task(models.Model):

    STATUSE_CHOISES = [
        ('todo', 'To do'),
        ('in_progres', 'In progres'),
        ('done', "Done")
    ]

    PRIORETY_CHOISES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('Hard', "Hard")
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUSE_CHOISES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORETY_CHOISES, default='easy')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    creater = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='tasks')
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs = {'pk': self.pk})


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete= models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="comments_media",blank=True,null=True)

    def get_absolute_url(self):
        return self.task.get_absolute_url()


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='liked_comments')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','comment')