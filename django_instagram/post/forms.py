from django import forms
from accounts.models import Profile
from post.models import Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)

class RepleForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea,max_length=200)

class SearchForm(forms.Form):
    word = forms.CharField(max_length=50)

class PostForm(forms. ModelForm):
    class Meta:
        model = Post
        fields = ('content','image',)
