# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_aluno_data_nasc'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='ano_entrada',
            field=models.CharField(default=b'', max_length=6),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluno',
            name='ativo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(default=b'', unique=True, max_length=11),
            preserve_default=True,
        ),
    ]
