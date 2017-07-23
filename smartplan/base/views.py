from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
# Home view
def home(request):
	return render(request, 'base/home.html', {})

# Home page for managing the data layer
def dataLayer(request):
	return render(request, 'base/dataLayer.html', {})