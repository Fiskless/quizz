from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from apps.users.forms import CreateUserForm, ChangeLoginColorForm


class UserRegisterView(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'


def change_login_color(request):
    if request.method == 'POST':
        form = ChangeLoginColorForm(request.POST, request=request)
        if form.is_valid():
            cd = form.cleaned_data
            color, spent_points = cd['login_color_field']
            request.user.points -= spent_points
            request.user.login_color = color
            request.user.save()
            return HttpResponseRedirect(reverse('main_page'))
    else:
        form = ChangeLoginColorForm(request=request)
    return render(request, 'change_color.html', {'form': form})