from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from apps.quizz.models import Poll, Question, Choice
from apps.users.models import CustomUser


@login_required
def show_all_polls(request):
    polls = Poll.objects.all()

    return render(request, 'main_page.html', {'polls': polls})


@login_required
def show_all_users_and_completed_polls(request):
    users = CustomUser.objects.all()

    return render(request, 'users_list.html', {'users': users})


def get_poll_detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    questions = poll.questions.all()
    context = {
        'questions': questions,
        'poll_id': poll_id
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

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'poll_id': poll_id,
            'error_message': "You didn't select a choice.",
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

