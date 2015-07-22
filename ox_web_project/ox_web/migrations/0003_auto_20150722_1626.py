# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 16, 26, 22, 200727, tzinfo=utc)),
        ),
    ]
