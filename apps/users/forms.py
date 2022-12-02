from django.contrib.auth.forms import UserCreationForm
from apps.users.models import CustomUser


class CreateUserForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username",)