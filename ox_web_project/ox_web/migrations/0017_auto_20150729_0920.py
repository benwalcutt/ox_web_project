# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0016_auto_20150729_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tag1',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='tag2',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='tag3',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='tag4',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
