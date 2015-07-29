# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0014_job_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='tags',
        ),
        migrations.AddField(
            model_name='job',
            name='tag1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='tag2',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='tag3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='tag4',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
