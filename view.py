from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage

questions = []
for i in xrange(1,30):
    questions.append({
        ‘title’: ‘title ‘ + str(i),
        ‘id’: i,
        ‘text’: ‘text’ + str(i),
    })


def index(request, page=None):
	#pager: paginator;
	return HttpResponse('TEST')
	#return  render(request,'ask/index.html', {'test' : 'hello'}})

def signup(request):
	
	return ("")	 