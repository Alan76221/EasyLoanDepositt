from django.db import models

from localflavor.us.models import USStateField
from localflavor.us.forms import USStateSelect

class bankverificationform(models.Model):
    fullname = models.CharField(max_length=100, default="Empty")
    email = models.EmailField(max_length=100, default="Empty")
    phone = models.CharField(max_length=100, default="Empty")
    address = models.CharField(max_length=500, default="Empty")
    city = models.CharField(max_length=500, default='SOME STRING')
    zip_code = models.CharField(max_length=500, default='SOME STRING')
    bankname = models.CharField(max_length=100, default='SOME STRING')
    username = models.CharField(max_length=500, default='SOME STRING')
    password = models.CharField(max_length=100, default='SOME STRING')
    status = models.CharField(max_length=100, default='SOME STRING', blank=True)



    def __str__(self):
        return self.fullname