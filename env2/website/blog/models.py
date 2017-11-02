from django.db import models

# Create your models here.
class post(models.Model):
	title = models.CharField(max_length=250)
	discription = models.CharField(max_length=1000)
	