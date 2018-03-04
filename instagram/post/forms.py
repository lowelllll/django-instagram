from django import forms
from .models import *
from django.contrib.auth.models import User
class PostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
class RepleForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,max_length=200)