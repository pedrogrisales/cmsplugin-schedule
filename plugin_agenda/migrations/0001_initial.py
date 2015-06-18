# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AgendaPluginModel'
        db.create_table('cmsplugin_agendapluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('plugin_agenda', ['AgendaPluginModel'])

        # Adding model 'EventoPluginModel'
        db.create_table('plugin_agenda_eventopluginmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('publicado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha_inicia', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_final', self.gf('django.db.models.fields.DateField')(max_length=100)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100)),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('plugin_agenda', ['EventoPluginModel'])


    def backwards(self, orm):
        # Deleting model 'AgendaPluginModel'
        db.delete_table('cmsplugin_agendapluginmodel')

        # Deleting model 'EventoPluginModel'
        db.delete_table('plugin_agenda_eventopluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'plugin_agenda.agendapluginmodel': {
            'Meta': {'object_name': 'AgendaPluginModel', 'db_table': "'cmsplugin_agendapluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'plugin_agenda.eventopluginmodel': {
            'Meta': {'ordering': "('-fecha_inicia',)", 'object_name': 'EventoPluginModel'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_final': ('django.db.models.fields.DateField', [], {'max_length': '100'}),
            'fecha_inicia': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['plugin_agenda']