from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from apps.users.models import CustomUser


class CreateUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username",)


COLOR_CHOICES = (
    ('green', 'Зеленый цвет - 50 баллов'),
    ('purple', 'Фиолетовый цвет - 100 баллов'),
    ('blue', 'Синий  цвет - 150 баллов'),
)


class ChangeLoginColorForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ChangeLoginColorForm, self).__init__(*args, **kwargs)

    login_color_field = forms.ChoiceField(
        choices=COLOR_CHOICES,
        label='В какой цвет хотите покрасить?')

    def clean_login_color_field(self):
        login_color_field = self.cleaned_data['login_color_field']
        user_points = self.request.user.points
        color_to_cost = {
            'green': 50,
            'purple': 100,
            'blue': 150,
        }
        if user_points < color_to_cost[login_color_field]:
            raise ValidationError('Недостаточно баллов для покраски')
        return login_color_field, color_to_cost[login_color_field]


