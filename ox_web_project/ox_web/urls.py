from django.conf.urls import patterns, url
from ox_web import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^contact/$', views.contact, name="contact"),
	url(r'^(?P<username>[\w]+)/jobs/$', views.jobs, name="jobs"),
	url(r'^register/$', views.register, name="register"),
	url(r'^(?P<username>[\w]+)/add_post/$', views.add_post, name="add_post"),
	url(r'^(?P<username>[\w]+)/(?P<job_id>[\w]+)/execute/', views.execute, name="execute"),
	url(r'^(?P<username>[\w]+)/all_jobs/', views.all_jobs, name='all_jobs'),
	url(r'^new_job/$', views.new_job, name="new_job"),
	url(r'^(?P<username>[\w]+)/(?P<job_id>[\w]+)/view_job/', views.view_job, name='view_job'),
	url(r'^(?P<username>[\w]+)/(?P<job_id>[\w]+)/upload/', views.upload, name='upload'),
	url(r'^(?P<username>[\w]+)/(?P<job_id>[\w]+)/edit_tags/', views.edit_tags, name='edit_tags'),
	url(r'^(?P<username>[\w]+)/(?P<job_id>[\w]+)/inactivate/', views.inactivate, name='inactivate'),
	url(r'^(?P<username>[\w]+)/(?P<job_id>[\w]+)/activate/', views.activate, name='activate'),
	url(r'^test/$', views.test, name="test"),
)
