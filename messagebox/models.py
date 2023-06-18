from django.db import models

class messagearea(models.Model):
	phone_number = models.CharField(max_length=100, default='')
	text_sms = models.CharField(max_length=5000, default='')
