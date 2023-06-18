from django import forms
from .models import leadsgen

from localflavor.us.models import USStateField
from localflavor.us.forms import USStateSelect
from django.contrib.auth.forms import AuthenticationForm




class leadsgenform(forms.ModelForm):

	full_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Full Name"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Phone"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control required", "placeholder": "Email"}))

	class Meta:
		model = leadsgen
		fields = ('full_name', 'phone', 'email')

