from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import DataTable
from django.db.models.query import QuerySet

@login_required(login_url='/login/')
# Home view
def home(request):
	return render(request, 'base/home.html', {})

# Home page for managing the data layer
def dataLayer(request):
	return render(request, 'base/dataLayer.html', {})

class ListDataTables(ListView):
    model = DataTable
    context_object_name = "data_tables_of_data_layer"
    template_name = "base/dataLayer.html"
    
    def get_queryset(self):
    	return DataTable.objects.filter(dataLayer=self.kwargs['id_company'])