from __future__ import unicode_literals

from django.db import models

# Create your models here.




class store(models.Model):

	name =  models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	address = models.CharField(max_length=250)
	max_number_of_customer_at_one_time = models.CharField(max_length=250)
	working_driver = models.CharField(max_length=250)
	date_created = models.CharField(max_length=250)
	UID = models.CharField(max_length=250)
	is_deleted = models.CharField(max_length=250)
	discription = models.CharField(max_length=250)
	contact_first = models.CharField(max_length=250)
	contact_last = models.CharField(max_length=250)
	rating = models.CharField(max_length=250)
	number = models.CharField(max_length=250)
	#picture = models.ImageField()
	#alcohols = models.ManyToManyField(alcohol)

	
	def __str__(self):
		return self.name

	def __repr__(self):
		return "name: "+ self.name+'\n'+"location: "+self.location+'\n'+"address: "+self.address+'\n'+"max number of customer: "+self.max_number_of_customer_at_one_time+'\n'+"working_driver: "+self.working_driver+'\n'+"date created: "+self.date_created+'\n'+"UID: "+self.UID
		+'\n'+"is deleted: "+self.is_deleted+'\n'+"description: "+self.description+'\n'+"contact's firstname: "+self.contact_first+'\n'+"contact's lastname"+self.contact_last+'\n'+"rating: "+self.rating+'\n'+"number: "+self.number


class alcohol(models.Model):
	name = models.CharField(max_length=250) 
	price = models.FloatField(max_length=250)
	quantity = models.IntegerField()
	volume = models.IntegerField()
	brand = models.CharField(max_length=250)
	Type = models.CharField(max_length=250)
	subtype = models.CharField(max_length=250)
	origin = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	rating = models.IntegerField()
	available = models.BooleanField()
	#picture = models.ImageField()
	special = models.BooleanField()
	UID = models.IntegerField()
	number_sold = models.IntegerField()
	quantity_left = models.IntegerField()
	stores = models.ManyToManyField(store)
	
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return "name: "+ self.name+'\n'+"price: "+str(self.price)+'\n'+"quantity: "+str(self.quantity)+'\n'+"volume: "+str(self.volume)+'\n'+"brand: "+self.brand+'\n'+"Type: "+self.Type+'\n'+"subtype: "+self.subtype+'\n'+"origin: "+self.origin+'\n'+"description: "+self.description+'\n'+"rating: "+str(self.rating)+'\n'+"available: "+str(self.available)+'\n'+"special: "+str(self.special)+'\n'
		+'\n'+"UID: "+str(self.UID)+'\n'+"number sold: "+str(self.number_sold)+"quantity: "+str(self.quantity_left)+"stores: "+self.stores


#a = alcohol(name="Corona",price=0.99,quantity=100,volume=100,brand="Corona",Type="beer",subtype="beer",origin="US",description="Horse Piss",rating=4,available=True, special=True,UID=123,number_sold=120,quantity_left=30)



