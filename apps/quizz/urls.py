from django.urls import path

from apps.quizz.views import get_poll, get_results, show_all_polls, \
    show_all_users

urlpatterns = [
    path('', show_all_polls, name='main_page'),
    path('users_and_polls', show_all_users, name='users_and_polls'),
    path('poll/<int:poll_id>/', get_poll, name='poll'),
    path('poll/<int:poll_id>/results/', get_results, name='result_page'),
]