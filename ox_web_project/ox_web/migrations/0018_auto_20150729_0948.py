# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0017_auto_20150729_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tag1',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='tag2',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='tag3',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='tag4',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
