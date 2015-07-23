# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0009_auto_20150722_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='data_path',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='output_path',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
