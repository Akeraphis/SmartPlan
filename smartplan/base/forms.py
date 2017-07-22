from django import forms

#Login form for the user
class LoginForm(forms.Form):
	username = forms.CharField(label="User Name", max_length=40)
	password = forms.CharField(label="Password", widget=forms.PasswordInput)