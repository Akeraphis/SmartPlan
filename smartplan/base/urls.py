from django.conf.urls import url
from . import views

from .models import DataTable


urlpatterns = [
    url(r'^$', views.home),
    url(r'^dataLayer/(?P<id_company>\d+)$', views.ListDataTables.as_view(), name="data_layer"),
]
	