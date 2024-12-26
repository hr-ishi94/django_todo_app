from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Todo

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']   
   

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
    