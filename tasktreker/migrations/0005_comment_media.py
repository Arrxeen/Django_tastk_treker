# Generated by Django 5.1.1 on 2024-10-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasktreker', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='comments_media'),
        ),
    ]
