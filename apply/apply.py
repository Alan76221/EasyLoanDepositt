from django import forms
from .models import SnippetNew
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
class SnippetFormTwo(forms.ModelForm):

	class Meta:
		model = SnippetNew
		fields = ('name', 'email', 'phone', 'loan', 'address', 'city', 'state', 'zip_code')


