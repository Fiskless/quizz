from django.urls import path

from apps.quizz.views import get_vote_results, show_all_polls, \
    show_all_users_and_completed_polls, get_poll_detail, get_question_detail, \
    get_votes_for_question

urlpatterns = [
    path('', show_all_polls, name='main_page'),
    path('users_and_polls/',
         show_all_users_and_completed_polls,
         name='users_and_polls'),
    path('poll/<int:poll_id>/', get_poll_detail, name='poll_detail'),
    path('poll/<int:poll_id>/question/<int:question_id>/',
         get_question_detail,
         name='question_detail'),
    path('poll/<int:poll_id>/question/<int:question_id>/vote',
         get_votes_for_question,
         name='vote'),
    path('poll/<int:poll_id>/question/<int:question_id>/results/',
         get_vote_results,
         name='result_page'),
]