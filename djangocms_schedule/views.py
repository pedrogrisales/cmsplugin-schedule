#encoding:utf-8

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from models import EventModel
from datetime import datetime


def event_detail(request, slug):
    data = {}
    data['instance'] = get_object_or_404(EventModel,slug=slug)
    data['nexts'] = EventModel.objects.filter(
        published=True,
         #start_date__gte=datetime.now
    ).order_by('start_date')[:6]
    return render_to_response("djangocms_schedule/event_detail.html", data, context_instance=RequestContext(request))


def events(request):
    data = {}
    data['nexts'] = EventModel.objects.filter(
        published=True,
         #start_date__gte=datetime.now
    ).order_by('start_date')
    return render_to_response("djangocms_schedule/events.html", data, context_instance=RequestContext(request))
