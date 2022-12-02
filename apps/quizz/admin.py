from django.contrib import admin

# Register your models here.
from .models import Poll, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    list_display = ['__all__']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    list_display = ['__all__']


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]


