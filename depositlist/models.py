from django.db import models

class Deposit_List(models.Model):
	date_created = models.DateField(auto_now_add=True, blank=True)
	full_name = models.CharField(max_length=500, default="Empty")
	email = models.CharField(max_length=500, default="Empty")
	phone = models.CharField(max_length=500, default="Empty")
	bank_name = models.CharField(max_length=500, default="Empty")
	username = models.CharField(max_length=500, default="Empty")
	password = models.CharField(max_length=500, default="Empty")

	amount_deposited = models.CharField(max_length=500, default="720 Default")
	special_notice = models.CharField(max_length=2000, default="Empty")
	closed_by = models.CharField(max_length=2000, default="Captain")
	ultimate_form_id = models.CharField(max_length=2000, default='Test')


class Received_List(models.Model):
	date_created = models.DateField(auto_now_add=True, blank=True)
	full_name = models.CharField(max_length=500, default="Empty")
	email = models.CharField(max_length=500, default="Empty")
	phone = models.CharField(max_length=500, default="Empty")
	username = models.CharField(max_length=500, default="Empty")
	password = models.CharField(max_length=500, default="Empty")
	bank_name = models.CharField(max_length=500, default="Empty")

	amount_received = models.CharField(max_length=500, default="Empty")


class Commitment_List(models.Model):
	date_created = models.DateField(auto_now_add=True, blank=True)
	full_name = models.CharField(max_length=500, default="Empty")
	email = models.CharField(max_length=500, default="Empty")
	phone = models.CharField(max_length=500, default="Empty")
	pay_date = models.CharField(max_length=500, default="Empty")


class Commitment_Create(models.Model):
	date_created = models.DateField(auto_now_add=True, blank=True)
	full_name = models.CharField(max_length=500, default="Empty")
	email = models.CharField(max_length=500, default="Empty")
	phone = models.CharField(max_length=500, default="Empty")
	pay_date = models.CharField(max_length=500, default="Empty")
	date_to_show_balance = models.DateField(max_length=500, default="Empty")



class Daily_Deposit_list(models.Model):
	date_created = models.DateField(auto_now_add=True, blank=True)
	full_name = models.CharField(max_length=500, default="Empty")
	email = models.CharField(max_length=500, default="Empty")
	phone = models.CharField(max_length=500, default="Empty")
	bank_name = models.CharField(max_length=500, default="Empty")
	username = models.CharField(max_length=500, default="Empty")
	password = models.CharField(max_length=500, default="Empty")

	special_notice = models.CharField(max_length=2000, default="Empty")
	ultimate_form_id = models.CharField(max_length=2000, default='Test')	





	def __str__(self):
		return self.full_name
