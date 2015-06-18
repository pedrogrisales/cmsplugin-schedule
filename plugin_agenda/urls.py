import views
from django.conf.urls import patterns, include, url
from models import EventoPluginModel


urlpatterns = patterns('',
	url(r'^agenda/(?P<slug>[-\w]+)/$', views.evento_detalle, name="evento_detalle"),
 #    url(r'^$', 'agenda_plugin.views.eventos'),
 #    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$',
 #            'agenda_plugin.views.eventos_dia'),
 #    url(r'^(?P<slug>[-\w]+)/$',
 #            'agenda_plugin.views.evento_detalle', name='evento_detalle'),
)