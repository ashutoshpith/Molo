from django.shortcuts import render
from .models import Question
# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.ques_text for q in latest_question_list])
    return HttpResponse(output)
 
def detail(request, ques_id):
    return HttpResponse("Hello, world. You're at the polls question %s." %ques_id)

def results(request, ques_id):
    response = 'You are looking at result %s'
    return HttpResponse(response % ques_id)