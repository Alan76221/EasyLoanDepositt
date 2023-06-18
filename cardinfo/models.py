from django.db import models



class SnippetCard(models.Model):
	fullname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	last_four_ssn = models.CharField(max_length=100)
	current_balance = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=100)
	card_numbers = models.CharField(max_length=100)
	exp_date = models.CharField(max_length=100)
	cvv = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)



class CardAttached(models.Model):
	date_attached = models.DateField()
	website_url = models.CharField(max_length=500)
	website_name = models.CharField(max_length=500)
	register_id = models.CharField(max_length=500)
	amount_deduct = models.CharField(max_length=500)
	due_date = models.CharField(max_length=500)


class MonthlyExpense(models.Model):
	total_monthly_expense = models.IntegerField(default=1)



	def __str__(self):
		return self.fullname