from django.db import models

# Create your models here.
class CannedResponse(models.Model):
	canned_name = models.CharField(max_length=500)
	canned = models.TextField(default='')


class CheckReclose(models.Model):
	canned_name = models.CharField(max_length=500)
	canned = models.TextField(default='')

class PaydayReclose(models.Model):
	canned_name = models.CharField(max_length=500)
	canned = models.TextField(default='')



	def __str__(self):
		return self.canned_name


