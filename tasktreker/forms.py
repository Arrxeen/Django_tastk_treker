from django.forms import ModelForm
from .models import Task
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','status','priority','due_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
  

        self.fields["due_date"].widget = forms.DateTimeInput(attrs={"type": "datetime-local"})