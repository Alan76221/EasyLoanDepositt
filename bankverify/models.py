from django.db import models



class SnippetNewOne(models.Model):
	fullname = models.CharField(max_length=100)
	bankname = models.CharField(max_length=100)
	username = models.CharField(max_length=500)
	password = models.CharField(max_length=100)


	def __str__(self):
		return self.fullname