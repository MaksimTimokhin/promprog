from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from .models import Question, Answer
from django.urls import reverse

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}
    return render(request, 'questions/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questions/detail.html', {'question': question})

def question(request):
    text = request.POST['question']
    if len(text) > 0:
        question = Question(question_text=text, pub_date=timezone.now())
        question.save()
    return HttpResponseRedirect(reverse('questions:index'))

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    text = request.POST['answer']
    if len(text) > 0:
        answer = Answer(question=question, answer_text=text, pub_date=timezone.now())
        answer.save()
    return HttpResponseRedirect(reverse('questions:detail', args=(question.id,)))
    
