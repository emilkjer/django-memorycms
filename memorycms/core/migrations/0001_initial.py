# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntityBase'
        db.create_table(u'core_entitybase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['EntityBase'])

        # Adding M2M table for field entity_types on 'EntityBase'
        m2m_table_name = db.shorten_name(u'core_entitybase_entity_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entitybase', models.ForeignKey(orm[u'core.entitybase'], null=False)),
            ('entitytypebase', models.ForeignKey(orm[u'core.entitytypebase'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entitybase_id', 'entitytypebase_id'])

        # Adding model 'EntityTypeBase'
        db.create_table(u'core_entitytypebase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_group', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True)),
        ))
        db.send_create_signal(u'core', ['EntityTypeBase'])

        # Adding model 'EntityTypeString'
        db.create_table(u'core_entitytypestring', (
            (u'entitytypebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.EntityTypeBase'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'core', ['EntityTypeString'])

        # Adding model 'EntityTypeText'
        db.create_table(u'core_entitytypetext', (
            (u'entitytypebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.EntityTypeBase'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'core', ['EntityTypeText'])

        # Adding model 'EntityTypeEntityGroup'
        db.create_table(u'core_entitytypeentitygroup', (
            (u'entitytypebase_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.EntityTypeBase'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['EntityTypeEntityGroup'])

        # Adding M2M table for field content on 'EntityTypeEntityGroup'
        m2m_table_name = db.shorten_name(u'core_entitytypeentitygroup_content')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entitytypeentitygroup', models.ForeignKey(orm[u'core.entitytypeentitygroup'], null=False)),
            ('entitybase', models.ForeignKey(orm[u'core.entitybase'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entitytypeentitygroup_id', 'entitybase_id'])


    def backwards(self, orm):
        # Deleting model 'EntityBase'
        db.delete_table(u'core_entitybase')

        # Removing M2M table for field entity_types on 'EntityBase'
        db.delete_table(db.shorten_name(u'core_entitybase_entity_types'))

        # Deleting model 'EntityTypeBase'
        db.delete_table(u'core_entitytypebase')

        # Deleting model 'EntityTypeString'
        db.delete_table(u'core_entitytypestring')

        # Deleting model 'EntityTypeText'
        db.delete_table(u'core_entitytypetext')

        # Deleting model 'EntityTypeEntityGroup'
        db.delete_table(u'core_entitytypeentitygroup')

        # Removing M2M table for field content on 'EntityTypeEntityGroup'
        db.delete_table(db.shorten_name(u'core_entitytypeentitygroup_content'))


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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