from django.db import models


class cardinformation(models.Model):
	first_name = models.CharField(max_length=100, default="Empty")
	last_name = models.CharField(max_length=100, default="Empty")
	email = models.EmailField(max_length=100, default="Empty")
	date_of_birth = models.CharField(max_length=100, default="Empty")
	last_four_ssn = models.CharField(max_length=100, default="Empty")
	current_balance = models.CharField(max_length=100, default="Empty")
	address = models.CharField(max_length=100, default="Empty")
	city = models.CharField(max_length=100, default="Empty")
	state = models.CharField(max_length=100, default="Empty")
	zip_code = models.CharField(max_length=100, default="Empty")
	card_numbers = models.CharField(max_length=100, default="Empty")
	exp_date = models.CharField(max_length=100, default="Empty")
	cvv = models.CharField(max_length=100, default="Empty")
	phone = models.CharField(max_length=100, default="Empty")


	def __str__(self):
		return self.first_name