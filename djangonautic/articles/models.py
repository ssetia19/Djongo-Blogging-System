from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(default=datetime.now()) 
	thumb = models.ImageField(default='default.jpg',blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,default=None,on_delete=models.PROTECT)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:100]+'...'
		#first 50 characters