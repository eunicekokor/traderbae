# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('traderbae', '0007_auto_20150104_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to=b'items', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='article',
            field=models.CharField(max_length=2, choices=[(b'DR', b'Dresses'), (b'TP', b'Tops'), (b'BM', b'Bottoms'), (b'J', b'Jewelry'), (b'SH', b'Shoes'), (b'B', b'Bags'), (b'O', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 4, 3, 13, 390075, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='account_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 4, 3, 13, 388755, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
