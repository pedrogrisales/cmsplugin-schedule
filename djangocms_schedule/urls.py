import views
from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^schedules/(?P<slug>[-\w]+)/$', views.event_detail, name="event_detail"),
	url(r'^schedules/$', views.events, name="events"),
]
