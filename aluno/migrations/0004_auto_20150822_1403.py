# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_auto_20150822_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='ano_entrada',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(unique=True, max_length=11),
            preserve_default=True,
        ),
    ]
