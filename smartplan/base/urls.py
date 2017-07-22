from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login$', views.logIn, name='login'),
    url(r'^dataLayer$', views.dataLayer),
    url(r'^logout$', views.logOut, name="logout")
]
