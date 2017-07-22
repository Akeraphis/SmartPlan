from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.core.urlresolvers import reverse

# Home view
def home(request):
	return render(request, 'base/home.html', {})

# Login view - Login to the solution
def logIn(request):
	error = False

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleansed_data["username"]
			password = form.cleansed_data["password"]
			user = authenticate(username=username, password=password)

			if user:
				login(request, error)
			else:
				error = True
	else:
		form = LoginForm()

	return render(request, 'base/login.html', locals())

# Logout view
def logOut(request):
	logout(request)
	return redirect(reverse(home))

# Home page for managing the data layer
def dataLayer(request):
	return render(request, 'base/dataLayer.html', {})