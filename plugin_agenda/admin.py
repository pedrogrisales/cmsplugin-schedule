from django.contrib import admin
from django.utils.translation import ugettext as _
from cms.admin.placeholderadmin import PlaceholderAdmin


from django.forms import ModelForm

#from suit_redactor.widgets import RedactorWidget
from cms.forms.widgets import PluginEditor


from models import AgendaPluginModel, EventoPluginModel


class AgendaAdmin(PlaceholderAdmin):
    fieldsets = [
        ('Datos', {'classes': ('full-width',),
         'fields': ('publicado', 'fecha_inicia', 'fecha_final', 'nombre','hora','detalle')}),
        ('Descripcion detalle', {'classes': ('full-width',), 'fields': ('contenido',)}),
    ]

    date_hierarchy = 'fecha_creacion'
    list_display = ('fecha_creacion','nombre', 'fecha_inicia', 'fecha_final', 'publicado')
    list_display_links = ('nombre',)
    list_filter = ('nombre', )

    class Media:
        js = ( 'js/jquery.min.js',)


admin.site.register(EventoPluginModel, AgendaAdmin)



