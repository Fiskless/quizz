from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.quizz.models import Poll


class CustomUser(AbstractUser):
    points = models.PositiveSmallIntegerField('Количество баллов', default=0)
    completed_polls = models.ManyToManyField(Poll,
                                             related_name="users",
                                             verbose_name='Пройденный опросы'
                                             )

    def __str__(self):
        return self.username
