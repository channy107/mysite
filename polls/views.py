from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question, Choice
from django.utils import timezone


def input(request):
    return render(request, 'polls/input.html', {})

def add_question(request):
    text = request.POST['text']
    q = Question(
        question_text=text,
        pub_date=timezone.now())
    q.save()
    # return render(request, 'polls/.html', {})
    return HttpResponse('입력완료')


def data(request):
    value = request.GET['user_name']
    return HttpResponse

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes + 1
    c.save()

    return render(request, 'polls/vote.html', {})


def detail(request,id):
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item':question})


def index(request):

    list = Question.objects.all()
    return render(request, 'polls/index.html', {'question': list})
