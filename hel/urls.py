from django.conf.urls import patterns, url
from hel import views

urlpatterns = patterns('hel.views',
url(r'^$', 'index', name='index'), 
)