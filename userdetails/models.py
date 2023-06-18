from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length=500, default='')
	address = models.CharField(max_length=500, default='')
	loan_amount = models.IntegerField(default=2000	)
	monthly_installment = models.FloatField(default=91.25)
	total_repayback = models.IntegerField(default=2190)
	payment_date = models.CharField(max_length=500, default='')
	tracking_no = models.CharField(max_length=500, default='54213')
	tracking_status = models.CharField(max_length=500, default='Verification Pending')
	lending_description = models.CharField(max_length=500, default='')
	full_name = models.CharField(max_length=500, default=''),

	def __str__(self):
		return self.user.username
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
	
