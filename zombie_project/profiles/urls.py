from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns(' ',
	url(r'^$', views.index, name = 'index'),
	url(r'^status/$', views.status, name = 'status'),
	url(r'^badges/$', views.badges, name = 'badges'),
)