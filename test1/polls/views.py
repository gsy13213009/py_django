from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader

from polls.models import Question


def index(request):
    last_question_list = Question.objects.order_by('pub_date');
    context = {
        'latest_question_list': last_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("you are looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse("you are voting at the of question %s" % question_id)
