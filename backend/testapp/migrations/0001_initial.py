# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ParentClass'
        db.create_table(u'testapp_parentclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('superclass', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'testapp', ['ParentClass'])

        # Adding model 'Child1'
        db.create_table(u'testapp_child1', (
            (u'parentclass_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['testapp.ParentClass'], unique=True, primary_key=True)),
            ('child1field', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'testapp', ['Child1'])

        # Adding model 'Child2'
        db.create_table(u'testapp_child2', (
            (u'parentclass_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['testapp.ParentClass'], unique=True, primary_key=True)),
            ('child2field', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal(u'testapp', ['Child2'])


    def backwards(self, orm):
        # Deleting model 'ParentClass'
        db.delete_table(u'testapp_parentclass')

        # Deleting model 'Child1'
        db.delete_table(u'testapp_child1')

        # Deleting model 'Child2'
        db.delete_table(u'testapp_child2')


    models = {
        u'testapp.child1': {
            'Meta': {'object_name': 'Child1', '_ormbases': [u'testapp.ParentClass']},
            'child1field': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'parentclass_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['testapp.ParentClass']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'testapp.child2': {
            'Meta': {'object_name': 'Child2', '_ormbases': [u'testapp.ParentClass']},
            'child2field': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'parentclass_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['testapp.ParentClass']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'testapp.parentclass': {
            'Meta': {'object_name': 'ParentClass'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superclass': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['testapp']