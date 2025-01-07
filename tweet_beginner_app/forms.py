from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    city = forms.CharField(required=False, help_text='Enter city name for weather info')
    
    class Meta:
        model = Tweet
        fields = ['text', 'photo', 'city']

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
