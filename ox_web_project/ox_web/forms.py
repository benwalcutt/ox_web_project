from django import forms
from django.contrib.auth.models import User
from ox_web.models import UserProfile, Blog
from django.utils import timezone

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('website',)

class BlogPost(forms.ModelForm):
  title = forms.CharField(max_length=100)
  slug = forms.SlugField(max_length=100)
  body = forms.CharField(widget=forms.Textarea)
  posted = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

  class Meta:
    model = Blog
    fields = ('title', 'slug', 'body', 'posted',)
