from django.db import models



class infograb(models.Model):
	phone = models.CharField(max_length=100)
	ssn = models.EmailField(max_length=100)
	


	def __str__(self):
		return self.phone