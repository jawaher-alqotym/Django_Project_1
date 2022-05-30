from django import forms
from .models import *

class UserForm(forms.ModelForm):
 #password_input = forms.CharField(label=-("Password"), widget=forms.PasswordInput)
 class Meta:
  model = User
  fields = ('user_name', 'first_name', 'last_name', 'email', 'password')