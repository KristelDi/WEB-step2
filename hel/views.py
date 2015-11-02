from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def FuncHello(request):
# 	return HttpResponse("Hello World!")
def FuncHello(request):
	if request.method == 'GET':
	    test = "GET HELLO WORLD";
	elif request.method == 'POST':
	    test = "post"
	return  HttpResponse(test)