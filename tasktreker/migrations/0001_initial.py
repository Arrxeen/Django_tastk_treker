# Generated by Django 5.1.1 on 2024-10-06 12:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('todo', 'To do'), ('in_progres', 'In progres'), ('done', 'Done')], default='todo', max_length=20)),
                ('priority', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('Hard', 'Hard')], default='easy', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]