from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
  
        self.fields["due_date"].widget = forms.DateTimeInput(attrs={"type": "datetime-local"})

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date']


class TaskFilterForm(forms.Form):
    
    STATUSE_CHOISES = [
        ('','All'),
        ('todo', 'To do'),
        ('in_progres', 'In progres'),
        ('done', "Done")
    ]
        
    status = forms.ChoiceField(choices=STATUSE_CHOISES, required=False , label = "status")