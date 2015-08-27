# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0004_auto_20150824_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='cpf',
            field=models.CharField(default=0, max_length=11),
            preserve_default=False,
        ),
    ]
