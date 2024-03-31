from django.db import models
class cardinformation(models.Model):
    loan_choices = (
('$3000', '$3000 for 36 months = $90.83 each month. (Your total payback to the company would be $3270 with interest rate 9%)'),
('$1000', '$1000 for 12 months = $90.83 each month. (Your total payback to the company would be $1090 with interest rate 9%)'),
('$1500', '$1500 for 12 months = $136.25 each month. (Your total payback to the company would be $1090 with interest rate 9%)'),
('$2000', '$2000 for 24 months = $90.83 each month. (Your total payback to the company would be $2180 with interest rate 9%)'),
('$2500', '$2500 for 24 months = $113.54 each month. (Your total payback to the company would be $2180 with interest rate 9%)'),
('$3000', '$3000 for 36 months = $90.83 each month.. (Your total payback to the company would be $3270 with interest rate 9%)'),
('$3500', '$3500 for 36 months = $105.97 each month. (Your total payback to the company would be $2180 with interest rate 9%)'),
('$4000', '$4000 for 48 months = $90.83 each month. (Your total payback to the company would be $4360 with interest rate 9%)'),
('$4500', '$4500 for 48 months = $102.18 each month. (Your total payback to the company would be $4360 with interest rate 9%)'),
('$5000', '$5000 for 60 months = $90.83 each month. (Your total payback to the company would be $5450 with interest rate 9%)'),
('$5500', '$5500 for 60 months = $99.91 each month. (Your total payback to the company would be $5450 with interest rate 9%)'),
('$6000', '$6000 for 72 months = $90.83 each month. (Your total payback to the company would be $6540 with interest rate 9%)'),
('$6500', '$6500 for 72 months = $98.40 each month. (Your total payback to the company would be $6540 with interest rate 9%)'),
('$7000', '$7000 for 84 months = $90.83 each month. (Your total payback to the company would be $7630 with interest rate 9%)'),
('$7500', '$7500 for 84 months = $97.32 each month. (Your total payback to the company would be $7630 with interest rate 9%)'),
('$8000', '$8000 for 96 months = $90.83 each month. (Your total payback to the company would be $8720 with interest rate 9%)'), )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, blank=True, null=True)
    last_four_ssn = models.CharField(max_length=100, blank=True, null=True)
    current_balance = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    card_numbers = models.CharField(max_length=100, blank=True, null=True)
    exp_date = models.CharField(max_length=100, blank=True, null=True)
    cvv = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    loan_amount = models.CharField(max_length=100, choices=loan_choices, blank=True, null=True)
    payment_date = models.CharField(max_length=100, blank=True, null=True)  
    def __str__(self):
    	return self.first_name