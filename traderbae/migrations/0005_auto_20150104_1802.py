# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('traderbae', '0004_auto_20150104_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='account_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 2, 2, 0, 442979, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text=b'This will be your name around the site.', max_length=18),
            preserve_default=True,
        ),
    ]
