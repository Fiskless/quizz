from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic

from apps.users.forms import CreateUserForm


class UserRegisterView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
