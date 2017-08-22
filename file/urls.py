from django.conf.urls import url
from file import views

urlpatterns = [
	url(r'^$',views.Form),
	url(r'^upload/$', views.Upload),
]
