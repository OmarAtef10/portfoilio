from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['Username', 'Email', 'Subject', 'Message']

        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'Email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'Subject': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}),
            'Message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}),

        }
