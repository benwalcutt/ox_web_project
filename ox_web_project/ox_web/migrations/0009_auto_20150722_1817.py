# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0008_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
