# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('traderbae', '0003_auto_20150104_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 1, 10, 56, 8484, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='items',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 1, 5, 1, 11, 53, 408613, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2015, 1, 5, 1, 12, 15, 935623, tzinfo=utc), upload_to=b'users'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(default=b'Columbia', max_length=50),
            preserve_default=True,
        ),
    ]
