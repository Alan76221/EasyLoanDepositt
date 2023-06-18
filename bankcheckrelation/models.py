from django.db import models

class CheckRelation(models.Model):
	bank_name = models.CharField(max_length=500, default='')
	check_name = models.CharField(max_length=500, default='')
	highest_amount_deposited = models.CharField(max_length=500, default='')



	def __str__(self):
		return self.bank_name