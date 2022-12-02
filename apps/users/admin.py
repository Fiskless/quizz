from django.contrib import admin
from django.contrib.auth.models import User

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass


