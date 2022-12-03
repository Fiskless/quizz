from django.contrib import admin
from .models import Poll, Question, Choice


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    list_display = ['__all__']


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    list_display = ['__all__']
    readonly_fields = ['votes']


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]
    fields = ('poll', 'text')



