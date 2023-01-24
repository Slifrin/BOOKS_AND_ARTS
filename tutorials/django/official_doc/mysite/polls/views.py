from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render


from polls.models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index2(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist as e:
        raise Http404(f"Question with id {question_id} does not exist.")
    return render(request, 'polls/detail.html', {'question': question})

def detail_alternative(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    response = f"You are looking at results of question {question_id}"
    return HttpResponse(response)


def vote(request: HttpRequest, question_id):
    return HttpResponse(f"You are voting on question {question_id}")
