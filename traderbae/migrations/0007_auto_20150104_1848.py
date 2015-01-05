# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('traderbae', '0006_auto_20150104_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 2, 48, 19, 138665, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='account_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 2, 48, 19, 136972, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
