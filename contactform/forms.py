from django import forms
from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
class SnippetForm(forms.ModelForm):


	name = forms.CharField(widget=forms.TextInput(attrs={"class":"col-lg-12 col-md-12 col-sm-12 form-group contact-icon contacts-name", "placeholder": "Full Name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class":"col-lg-12 col-md-12 col-sm-12 form-group contact-icon contacts-name", "placeholder": "Email"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class":"col-lg-12 col-md-12 col-sm-12 form-group contact-icon contacts-name", "placeholder": "Phone Number"}))
	body = forms.CharField(widget=forms.TextInput(attrs={"class":"col-lg-12 col-md-12 col-sm-12 form-group contact-icon contacts-name", "placeholder": "Message"}))

	class Meta:
		model = Snippet
		fields = ('name', 'email', 'phone', 'body')
