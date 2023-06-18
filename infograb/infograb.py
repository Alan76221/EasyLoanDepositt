from django import forms
from .models import infograb
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm
class infograb(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Phone Number"}))
	ssn = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Last 4 digit of SSN"}))


	class Meta:
		model = infograb
		fields = ('phone', 'ssn')


