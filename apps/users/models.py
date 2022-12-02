from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    points = models.PositiveSmallIntegerField('Количество баллов', default=0)

    def __str__(self):
        return self.username
