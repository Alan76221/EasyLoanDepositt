from django.db import models

class leadsgen(models.Model):
	full_name = models.CharField(max_length=100, default="Empty") 
	phone = models.CharField(max_length=100, default="Empty") 
	email = models.EmailField(max_length=100, default="Empty")



	def __str__(self):
		return self.full_name