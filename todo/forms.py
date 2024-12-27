from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Todo

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"fieldclass"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"fieldclass"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"fieldclass"}))
    confirm_password= forms.CharField(widget=forms.PasswordInput(attrs={"class":"fieldclass"}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']   
   

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"fieldclass"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"fieldclass"}))
    
class TodoForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"class":"textareafield"}))
    
    class Meta:
        model = Todo
        fields = ['text']
    