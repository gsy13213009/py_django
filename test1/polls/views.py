from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from polls.models import Question


def index(request):
    last_question_list = Question.objects.order_by('pub_date');

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':last_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("you are looking at the detail of question %s"%question_id)

def results(request, question_id):
    return HttpResponse("you are looking at the results of question %s"%question_id)

def vote(request, question_id):
    return HttpResponse("you are voting at the of question %s"%question_id)