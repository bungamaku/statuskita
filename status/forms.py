from django import forms
from .models import StatusModel

class StatusForm(forms.Form):
    your_status = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form',
        'required': 'True',
        'placeholder': 'How are you today?',
    }))