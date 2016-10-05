from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import EventPluginModel, EventModel
from datetime import datetime


class SchedulePlugin(CMSPluginBase):
    model = EventPluginModel
    name = _("Plugin Schedule")
    render_template = EventPluginModel.PLUGIN_TEMPLATES[0][0]

    def render(self, context, instance, placeholder):
        if instance and instance.template:
            self.render_template = instance.template

        olist = EventModel.objects.filter(
            published=True,
            #start_date__gte=datetime.now
        ).order_by('start_date')
        if instance.number:
            context['olist'] = olist[:instance.number]
        else:
            context['olist'] = olist
        return context


plugin_pool.register_plugin(SchedulePlugin)
