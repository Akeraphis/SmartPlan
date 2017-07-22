from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse


# Home view
def home(request):
	return render(request, 'base/home.html', {})

# Home page for managing the data layer
def dataLayer(request):
	return render(request, 'base/dataLayer.html', {})

def dire_bonjour(request):
    if request.user.is_authenticated():
        return HttpResponse("Salut, {0} !".format(request.user.username))
    return HttpResponse("Salut, anonyme.")