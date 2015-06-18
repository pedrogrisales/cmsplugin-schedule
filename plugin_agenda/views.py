#encoding:utf-8

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from models import EventoPluginModel
from datetime import datetime    

# def eventos(request):
#     data = {}     
#     data['instancia'] = EventoModel.objects.all()
#     return render_to_response("agenda_plugin/eventos.html", data, context_instance=RequestContext(request))


# def eventos_dia(request, year, month, day):
#     data = {}     
#     data['instancia'] = EventoModel.objects.filter(start=date(int(year), int(month), int(day)))
#     return render_to_response("agenda_plugin/eventos-dia.html", data, context_instance=RequestContext(request))
   

def evento_detalle(request, slug):
    data = {}
    data['instancia'] = get_object_or_404(EventoPluginModel,slug=slug)
    data['proximos'] = EventoPluginModel.objects.filter(publicado=True, fecha_inicia__gte=datetime.now).order_by('fecha_inicia')[:6]
    return render_to_response("plugin_agenda/detalle-evento.html", data, context_instance=RequestContext(request))
    

