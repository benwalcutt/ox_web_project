# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0013_auto_20150723_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='tags',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
