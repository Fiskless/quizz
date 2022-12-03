from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.quizz.models import Poll, Question, Choice
from apps.users.models import CustomUser


@login_required
def show_all_polls(request):
    polls = Poll.objects.all()

    return render(request, 'main_page.html', {'polls': polls})


@login_required
def show_all_users_and_completed_polls(request):
    users = CustomUser.objects.all().prefetch_related('completed_polls')

    return render(request, 'users_list.html', {'users': users})


@login_required
def get_poll_detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    questions = poll.questions.all()
    context = {
        'questions': questions,
        'poll_id': poll_id,
        'answered': request.GET.get('answered'),
        'error_message': "Для завершения опроса ответьте минимум на один вопрос",
    }
    return render(request, 'poll_detail.html', context)


def get_question_detail(request, poll_id, question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question': question,
        'poll_id': poll_id
    }
    return render(request, 'question_detail.html', context)


@login_required
def get_votes_for_question(request, poll_id, question_id):

    question = Question.objects.get(id=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'poll_id': poll_id,
            'error_message': "Выберите ответ",
        }
        return render(request, 'question_detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('result_page', args=[poll_id, question.id]))


@login_required
def get_vote_results(request, poll_id, question_id):
    question = Question.objects.get(id=question_id)
    context = {
        'question': question,
        'poll_id': poll_id,
    }
    return render(request, 'result_page.html', context)


@login_required
def complete_poll(request, poll_id):
    is_poll_already_completed = True
    poll = Poll.objects.get(id=poll_id)
    poll_weight = poll.weight
    if poll not in request.user.completed_polls.all():
        is_poll_already_completed = False
        request.user.points += poll_weight
        request.user.completed_polls.add(poll)
        request.user.save()
    context = {
        'poll_weight': poll_weight,
        'poll_id': poll_id,
        'is_poll_already_completed': is_poll_already_completed
    }
    return render(request, 'poll_completion.html', context)

