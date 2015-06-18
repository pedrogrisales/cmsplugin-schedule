from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.core.urlresolvers import reverse
from django.template import defaultfilters
from django.db.models import permalink
from cms.models.fields import PlaceholderField

class AgendaPluginModel(CMSPlugin):
    PLUGIN_TEMPLATES = (
        ('plugin_agenda/widget.html', 'Widget'),
        #('plugin_agenda/barra.html', 'Barra'),
    )
    numero = models.IntegerField(default=0)
    template = models.CharField('Template', max_length=255,
                                choices = PLUGIN_TEMPLATES)



class EventoPluginModel(models.Model):
    fecha_creacion = models.DateField(auto_now_add=True)
    publicado = models.BooleanField(default=False)
    fecha_inicia = models.DateField(null=True,blank=True)
    fecha_final = models.DateField(max_length=100,blank=False)
    nombre = models.CharField(max_length=100,blank=False)
    detalle = models.BooleanField(default=False,verbose_name="Mostrar detalle")
    hora = models.CharField(max_length=50,blank=False)
    slug = models.SlugField(max_length=100,blank=False,unique=True)
    contenido = PlaceholderField('contenido')


    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre)
        super(EventoPluginModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

    @permalink
    def get_absolute_url(self):
        return ('evento_detalle', None, { 'slug': self.slug })

    class Meta:
        ordering = ('-fecha_inicia',)
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
