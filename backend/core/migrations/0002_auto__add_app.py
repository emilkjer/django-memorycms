# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'App'
        db.create_table(u'core_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('top_entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EntityBase'], null=True)),
        ))
        db.send_create_signal(u'core', ['App'])


    def backwards(self, orm):
        # Deleting model 'App'
        db.delete_table(u'core_app')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.app': {
            'Meta': {'object_name': 'App'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'top_entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EntityBase']", 'null': 'True'})
        },
        u'core.entitybase': {
            'Meta': {'object_name': 'EntityBase'},
            'entity_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.EntityTypeBase']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.entitytypebase': {
            'Meta': {'object_name': 'EntityTypeBase'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'core.entitytypeentitygroup': {
            'Meta': {'object_name': 'EntityTypeEntityGroup', '_ormbases': [u'core.EntityTypeBase']},
            'content': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.EntityBase']", 'symmetrical': 'False'}),
            u'entitytypebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.EntityTypeBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.entitytypestring': {
            'Meta': {'object_name': 'EntityTypeString', '_ormbases': [u'core.EntityTypeBase']},
            'content': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'entitytypebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.EntityTypeBase']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.entitytypetext': {
            'Meta': {'object_name': 'EntityTypeText', '_ormbases': [u'core.EntityTypeBase']},
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'entitytypebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.EntityTypeBase']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']