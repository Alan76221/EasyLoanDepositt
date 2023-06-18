from django.db import models




class autoclosesnippet(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    bankname = models.CharField(max_length=500)
    how_long_banking = models.CharField(max_length=100)
    monthly_income = models.CharField(max_length=100)
    send_time = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)


    def __str__(self):
        return self.first_name