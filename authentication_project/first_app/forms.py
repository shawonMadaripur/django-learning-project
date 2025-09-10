from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegesterForm(UserCreationForm):
  username = forms.CharField(help_text=None)
  password1 = forms.CharField(widget=forms.PasswordInput)
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']