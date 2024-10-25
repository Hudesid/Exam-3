from django import forms
from . import models


class EmailForm(forms.ModelForm):
    class Meta:
        model = models.Email
        fields = ('name', 'email', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Your Comment', 'class': 'form-control'}),
        }

