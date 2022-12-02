from django.contrib import admin

# Register your models here.
from .models import Poll, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    list_display = ['__all__']


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    list_display = ['__all__']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]


