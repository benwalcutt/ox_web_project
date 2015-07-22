from django.conf.urls import patterns, url
from ox_web import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^contact/$', views.contact, name="contact"),
	url(r'^(?P<username>[\w]+)/jobs/$', views.jobs, name="jobs"),
)
