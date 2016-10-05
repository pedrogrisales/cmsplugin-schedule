from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.core.urlresolvers import reverse
from django.db.models import permalink
from cms.models.fields import PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField

class EventPluginModel(CMSPlugin):
    PLUGIN_TEMPLATES = (
        ('djangocms_schedule/widget.html', 'Widget'),
    )
    number = models.IntegerField(default=0)
    template = models.CharField('Template', max_length=255,
                                choices = PLUGIN_TEMPLATES)


class EventModel(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_publication = models.DateField(blank=False)
    published = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(max_length=100, blank=False)
    hour = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=250, blank=True, unique=True)
    detail = HTMLField(blank=True, null=True)
    show_detail = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('event_detail', None, { 'slug': self.slug })

    class Meta:
        ordering = ('-start_date',)
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
