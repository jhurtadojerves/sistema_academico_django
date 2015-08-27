# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0005_professor_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='cpf',
            field=models.CharField(unique=True, max_length=11),
            preserve_default=True,
        ),
    ]
