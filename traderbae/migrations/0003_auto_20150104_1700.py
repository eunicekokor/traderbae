# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traderbae', '0002_auto_20150104_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='account_created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='items',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
    ]
