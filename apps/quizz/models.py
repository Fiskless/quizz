from django.db import models


class Poll(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название опроса')
    weight = models.PositiveSmallIntegerField(
        verbose_name='Число баллов за опрос',
        default=0
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name='Вопрос')

    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name='Опрос'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name='Вопрос'
    )
    name = models.CharField(verbose_name='Вариант ответа', max_length=200)
    votes = models.PositiveIntegerField('Количество голосов', default=0)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.name