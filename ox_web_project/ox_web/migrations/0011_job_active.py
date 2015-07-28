# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0010_auto_20150723_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
