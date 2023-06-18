from django.db import models


class allcounter(models.Model):
	ironman = models.IntegerField(max_length=100, default=0)
	captain = models.IntegerField(max_length=100, default=0)
	thor = models.IntegerField(max_length=100, default=0)
	total_collection = models.IntegerField(max_length=100, default=0)
	total_visitor = models.IntegerField(max_length=100, default=0)
	check_created = models.IntegerField(max_length=100, default=0)
	total_commitment = models.IntegerField(max_length=100, default=0)






	def __str__(self):
		return self.total_collection