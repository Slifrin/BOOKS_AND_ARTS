from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DeleteView):
    model = Question
    template_name = "polls/results.html"


def vote(request: HttpRequest, question_id):
    question: Question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice: Choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You dind't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print(reverse("polls:results", args=(question.id,)))
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
