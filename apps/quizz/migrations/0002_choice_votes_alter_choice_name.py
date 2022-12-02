# Generated by Django 4.1.3 on 2022-12-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество голосов'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Вариант ответа'),
        ),
    ]