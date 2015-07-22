# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ox_web', '0004_auto_20150722_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 16, 38, 13, 436237, tzinfo=utc)),
        ),
    ]
