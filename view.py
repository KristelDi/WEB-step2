from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage

def index(request, page=None):
	#pager: paginator;
	return  HttpResponse("")

def signup(request):
	
	return ("")	