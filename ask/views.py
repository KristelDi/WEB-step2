from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# questions = []
# for i in xrange(1,30):
# 	questions.append({
# 		'title' : 'title {}'.format(i),
# 		'id' : i,
# 		'text' : 'parampampam{}'.format(i),
# 		})

def getpost(request):
    out = "Hello! <br>";
    out += "GET data: <br>"
    for key, value in request.GET.iteritems():
        out += (key + ": " + value + "<br>")
    out += " POST data:" + "<br>"
    for key, value in request.POST.iteritems():
        out += (key + ": " + value + "<br>")
    return HttpResponse(out)

def index(request):
#	return render(request,'ask/index.html',content_type="application/xhtml+xml")
	return HttpResponse('index')

