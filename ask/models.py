from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class QuestionManager (models.Manager):

	def newest(self):
		return self.order_by('-id')
	def hot(self):
		return self.order_by('-rating')



class Question(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=255)
	text = models.TextField()
	rating = models.IntegerField(default=0, db_index=True)
	created = models.DateTimeField(default=datetime.datetime.now)

	objects = QuestionManager()

	def __unicode__(self):
		return self.title


class Answer(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	text = models.TextField()
	created = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return self.text