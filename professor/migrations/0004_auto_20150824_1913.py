# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0003_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='categoria',
            field=models.ForeignKey(related_name='<built-in function id>', default=False, to='professor.Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='coordenador',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
