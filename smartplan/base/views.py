from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from .models import DataTable, DataLayer
from django.db.models.query import QuerySet
from django.views.generic.detail import DetailView
from lib2to3.fixes.fix_input import context
from django.core.urlresolvers import reverse_lazy
from .forms import DataTableForm

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
	
class DetailDataTable(DetailView):
	context_object_name = "data_table"
	model = DataTable
	template ="datatable_detail.html"

class DataTableCreate(CreateView):
	model = DataTable
	form_class = DataTableForm
	success_url = reverse_lazy('data_layer', kwargs={'id_company': 1})
	
	def form_valid(self, form):
		candidate_dt = form.save(commit=False)
		candidate_dt.tableLink= "temp"
		candidate_dt.dataLayer = get_object_or_404(DataLayer, id = self.get_company())
		candidate_dt.save()
		string = "/base/dataLayer/"+self.get_company()
		return HttpResponseRedirect(string)
	
	def get_company(self):
		return self.kwargs.get('id_company')