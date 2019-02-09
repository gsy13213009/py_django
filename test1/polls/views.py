from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from polls.models import Question


def index(request):
    last_question_list = Question.objects.order_by('pub_date');
    output = ', '.join([q.question_text for q in last_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("you are looking at the detail of question %s"%question_id)

def results(request, question_id):
    return HttpResponse("you are looking at the results of question %s"%question_id)

def vote(request, question_id):
    return HttpResponse("you are voting at the of question %s"%question_id)