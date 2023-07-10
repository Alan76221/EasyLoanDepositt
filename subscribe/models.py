from django.db import models


class SubsNew(models.Model):
	subsname = models.CharField(max_length=100)
	black_check_number = models.IntegerField(max_length=100, default=503947156)
	amazon_check_number = models.IntegerField(max_length=100, default=5072595)
	diabetes_check_number = models.IntegerField(max_length=100, default=57045)
	treasury_check_number = models.IntegerField(default=44355757)
	total_collection = models.IntegerField(max_length=100, default=1)
	daily_collection = models.IntegerField(max_length=100, default=1)
	monthly_expense_total = models.IntegerField(max_length=100, default=1)
	daily_check_created = models.IntegerField(max_length=100, default=1)
	scott_new_check_number = models.IntegerField(max_length=100, default=50400395)
	final_scott =  models.IntegerField(max_length=100, default=50400395)
	scott_customer_number = models.IntegerField(max_length=100, default=17513)
	cashier2022_check_number = models.IntegerField(max_length=100, default=151)
	personal_check_number = models.IntegerField(max_length=100, default=151)

	def __str__(self):
		return self.subsname