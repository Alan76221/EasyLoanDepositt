from django import forms
from .models import bankverificationform

from localflavor.us.models import USStateField
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import AuthenticationForm
class bankform(forms.ModelForm):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Full Name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Email Address"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Phone"}))
	address = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Address"}))
	city = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "City"}))
	zip_code = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Zip Code"}))

	bankname = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Name"}))
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Username"}))
	password = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Password"}))
	status = forms.CharField(widget=USStateSelect(attrs={"class":"input101", "placeholder": "USStateSelect"}))

	class Meta:
		model = bankverificationform
		fields = ('fullname', 'email', 'phone', 'address', 'city', 'zip_code', 'bankname', 'username', 'password', 'status')

