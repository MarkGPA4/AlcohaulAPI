from __future__ import unicode_literals

from django.db import models

# Create your models here.
class storage(models.Model):
	beverage = models.CharField(mex_length=250)
	name =  models.CharField(mex_length=250)
	number = models.CharField(mex_length=250)
	store = models.CharField(mex_length=250)


class delivery(models.Model):
	time = models.CharField(mex_length=250)
	driver = models.CharField(mex_length=250)
	store = models.CharField(mex_length=250)
	destination = models.CharField(mex_length=250)



