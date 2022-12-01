from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import AbstractUser


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
