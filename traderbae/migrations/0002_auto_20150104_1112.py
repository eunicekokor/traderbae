# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('traderbae', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 4, 19, 12, 10, 362137, tzinfo=utc), verbose_name=b'date added'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='items',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
    ]
