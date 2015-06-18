from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import AgendaPluginModel, EventoPluginModel
from datetime import datetime


class AgendaPlugin(CMSPluginBase):    
    model = AgendaPluginModel
    name = _("Plugin Agenda")
    render_template = AgendaPluginModel.PLUGIN_TEMPLATES[0][0]
    

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template
        
        lista = EventoPluginModel.objects.filter(publicado=True, fecha_inicia__gte=datetime.now).order_by('fecha_inicia')
        if instance.numero:
            context['lista'] = lista[:instance.numero]
        else:
            context['lista'] = lista    
        return context



plugin_pool.register_plugin(AgendaPlugin)
