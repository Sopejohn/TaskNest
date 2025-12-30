from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
]
    
    title = forms.CharField(label="Task title", max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter the title of your task...'
    }))

    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        'placeholder': 'Write your description here'
    }))

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, initial='Medium', widget=forms.Select())

    due_date = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'type': 'date'
    }))

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']



