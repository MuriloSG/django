# tasks/forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date', 'completed')
        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'rows': 9,
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'completed': forms.CheckboxInput(attrs={ 
                'class': 'form-check-input'
            }),
        }
