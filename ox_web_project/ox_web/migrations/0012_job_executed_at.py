# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0011_job_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='executed_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
