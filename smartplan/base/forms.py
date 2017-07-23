from django import forms
from .models import DataTable

#Login form for the user
class DataTableForm(forms.ModelForm):
	class Meta:
		model = DataTable
		fields = ('name',)