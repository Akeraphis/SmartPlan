from django.conf.urls import url
from . import views

from .models import DataTable


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^dataLayer/(?P<id_company>\d+)$', views.ListDataTables.as_view(), name="data_layer"),
    url(r'^dataLayer/(?P<id_company>\d+)/dataTable/(?P<pk>\d+)$', views.DetailDataTable.as_view(), name='data_tables'),
    url(r'^dataLayer/(?P<id_company>\d+)/new$', views.DataTableCreate.as_view(), name='data_table_new'),
]
	