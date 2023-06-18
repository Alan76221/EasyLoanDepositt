from django.db import models

# Create your models here.
class RecloseResponse(models.Model):
	reclose_name = models.CharField(max_length=500)
	reclose_area = models.TextField(default='')



	def __str__(self):
		return self.reclose_name