from django.db import models
from django.conf import settings
from django.utils import timezone
import pykew.ipni as ipni


class Post(models.Model):
	"""Post is a class that describe blog posts"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text=models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title



class Species(models.Model):
	"""docstring for Species"""
	name = models.CharField(max_length=200)
	count= 0


	def search(self):
		print("self.name is: "+ self.name)
		result = ipni.search(self.name)
		self.count= result.size()

	def __str__(self):
		return self.name
