# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntityBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntityTypeBase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_group', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntityTypeEntityGroup',
            fields=[
                ('entitytypebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.EntityTypeBase')),
                ('content', models.ManyToManyField(to='core.EntityBase')),
            ],
            options={
            },
            bases=('core.entitytypebase',),
        ),
        migrations.CreateModel(
            name='EntityTypeString',
            fields=[
                ('entitytypebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.EntityTypeBase')),
                ('content', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=('core.entitytypebase',),
        ),
        migrations.CreateModel(
            name='EntityTypeText',
            fields=[
                ('entitytypebase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.EntityTypeBase')),
                ('content', models.TextField(default=b'')),
            ],
            options={
            },
            bases=('core.entitytypebase',),
        ),
        migrations.AddField(
            model_name='entitytypebase',
            name='content_type',
            field=models.ForeignKey(editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entitybase',
            name='entity_types',
            field=models.ManyToManyField(to='core.EntityTypeBase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='app',
            name='top_entity',
            field=models.ForeignKey(to='core.EntityBase', null=True),
            preserve_default=True,
        ),
    ]
