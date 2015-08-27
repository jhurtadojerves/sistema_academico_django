# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_formacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('formacao', models.ForeignKey(related_name='<built-in function id>', to='professor.Formacao')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
