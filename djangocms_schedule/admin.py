from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.forms import ModelForm
from models import EventModel


class ScheduleAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'date_created'
    list_display = ('date_created','title', 'start_date', 'end_date', 'published')
    list_display_links = ('title',)
    list_filter = ('title', )

admin.site.register(EventModel, ScheduleAdmin)
