from django.shortcuts import render 
from django.http import HttpResponse
from answers.models import Answer

import random

# Create your views here.

def answer_views(requests):
    answers = Answer.objects.all()
    answer = random.choice(answers)
    return render(requests, 'answer.html', context={'answer': answer})

    
