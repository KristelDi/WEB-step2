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
	'likes' : 30 + i,
	})	

def index(request, page=None):
    pager = Paginator(questions, 4)
    qlist = (pager.page(page or 1)).object_list
    count = len(questions) / 4 + ((len(questions) % 4) == 1);
    count_list = [];
    page = (page or 1);
    for i in xrange(1,count):
    	count_list.append(i);
    return render(request, 'ask/index.html', {
        'qlist': qlist,
        'page': int(page),
        'count_list': count_list,
   	})


def question (request, question_number=1):

    temp = questions;
    temp.sort(key=lambda x: x['id']);
    quest = temp[int(question_number) - 1];
    return render(request, 'ask/question.html', {
        'quest': quest,
   	})	

def signup(request):
	return render(request,'ask/signup.html')

def login(request):
	return render(request,'ask/login.html')
 

def ask(request):
	return render(request,'ask/ask.html')

 
def hot(request, page=None):
   # questions.sort(questions.likes);
    temp = questions;
    temp.sort(key=lambda x: x['likes'], reverse=True);
    quest = [];
    for i in xrange(0,5):
		quest.append(temp[i]);
   	#quest = quest.fetch(5)
    return render(request, 'ask/index.html', {
        'qlist': quest,
        'page': page,
 	})	



