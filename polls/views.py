from django.shortcuts import render
from .models import Question
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    
    return render(request, 'polls/index.html', context)
 
def detail(request, ques_id):
    return HttpResponse("Hello, world. You're at the polls question %s." %ques_id)

def results(request, ques_id):
    response = 'You are looking at result %s'
    return HttpResponse(response % ques_id)


def about(request):
    return render(request, 'polls/about.html')


def contact(req):
    return render(req, 'polls/contact.html')