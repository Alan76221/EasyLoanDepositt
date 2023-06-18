from django.db import models

LOAN_CHOICES = (
    ('one','$1000'),
    ('two', '$2000'),
    ('three','$3000'),
    ('four','$4000'),
    ('five','$5000'),
    ('six','$6000'),
    ('seven','$7000'),
    ('eight','$8000'),

)


class SnippetNew(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=100, default='')
	loan = models.CharField(max_length=100, choices=LOAN_CHOICES, default='one')
	address = models.CharField(max_length=500)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	zip_code = models.IntegerField(max_length=100, default='')
	black_check_number = models.IntegerField(max_length=100, default=503947156)


class Commitments(models.Model):
	full_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=100, default='')
	loan = models.CharField(max_length=100, choices=LOAN_CHOICES, default='one')
	commitment_date = models.DateField(max_length=500)
	notice = models.CharField(max_length=100)
	def __str__(self):
		return self.name