from django.db import models

# Create your models here.
class Cuisine(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Restaurant(models.Model):
	title = models.CharField(max_length=200)
	ratings = models.IntegerField()
	location = models.TextField()

	