from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from operator import itemgetter, attrgetter, methodcaller
# Create your views here.


questions = []
for i in xrange(1,30):
	questions.append({
	'title' : 'title {}'.format(i),
	'id' : i,
	'text' : 'smth {}'.format(i),
	'likes' : 30 - i,
	})	

def index(request, page=None):
    pager = Paginator(questions, 4)
    qlist = pager.page(page or 1)
    return render(request, 'ask/index.html', {
        'qlist': qlist.object_list,
        'page': page,
   	})


def question (request, question_number=1):
    quest = questions[int (question_number) - 1];
    return render(request, 'ask/question.html', {
        'quest': quest,
   	})	

def signup(request):
	return render(request,'ask/signup.html')

def login(request):
	return render(request,'ask/login.html')
 

def ask(request):
	return render(request,'ask/ask.html')

 
def hot(request):
   # questions.sort(questions.likes);
    temp = questions;
    temp.sort(key=lambda x: x['likes'], reverse=True);
    quest = [];
    for i in xrange(0,9):
		quest.append(temp[i]);
   	#quest = quest.fetch(5)
    return render(request, 'ask/hot.html', {
        'quest': quest,
  	})	
