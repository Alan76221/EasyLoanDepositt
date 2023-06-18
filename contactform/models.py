from django.db import models

class Snippet(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=100, default='')
	body = models.CharField(max_length=2000, default='')

	def __str__(self):
		return self.name
		

