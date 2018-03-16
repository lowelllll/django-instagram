from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

class RepleForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,max_length=200)