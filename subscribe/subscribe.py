from django import forms
from .models import SubsNew
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
class SubsSnippet(forms.ModelForm):
	subsname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Enter Email Address"}))

	class Meta:
		model = SubsNew
		fields = ('subsname',)


