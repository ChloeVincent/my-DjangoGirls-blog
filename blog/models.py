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
	"""This corresponds to the results returned by a query to pykew"""
	query = models.CharField(max_length=200)
	count= 0
	occurences =[]


	def search(self):
		results = ipni.search(self.query)
		self.occurences=[]

		self.count = results.size()
		for result in results:
			self.occurences.append(Occurence(result)) 


	def __str__(self):
		return self.query


class Occurence(models.Model):
	"""docstring for Occurence"""

	name = models.CharField(max_length=200)
	family = models.CharField(max_length=200)
	genus = models.CharField(max_length=200)
	species = models.CharField(max_length=200)
	distribution = models.CharField(max_length=200)

	def __init__(self,result):
		self.name = ""
		self.family = ""
		self.genus = ""
		self.species = ""
		self.distribution=""

		if 'name' in result.keys():
			self.name = result['name']
		if 'family' in result.keys():
			self.family = result['family']
		if 'genus' in result.keys():
			self.genus = result['genus']
		if 'species' in result.keys(): 
			self.species = result['species']
		if 'distribution' in result.keys():
			self.distribution =result['distribution']



	def __str__(self):
		return self.name
