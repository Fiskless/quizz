# Generated by Django 4.1.3 on 2022-12-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_choice_votes_alter_choice_name'),
        ('users', '0003_alter_customuser_completed_polls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='completed_polls',
            field=models.ManyToManyField(blank=True, related_name='users', to='quizz.poll', verbose_name='Пройденный опросы'),
        ),
    ]