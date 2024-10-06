from django.db import models
from django.contrib.auth.models import User
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