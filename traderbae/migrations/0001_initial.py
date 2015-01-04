# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=20)),
                ('article', models.CharField(max_length=2, choices=[(b'DR', b'Dresses'), (b'TP', b'Tops'), (b'BM', b'Bottoms'), (b'J', b'Jewelry'), (b'SH', b'Shoes'), (b'O', b'Other')])),
                ('color', models.CharField(max_length=10)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('likes', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to=b'items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(help_text=b'This will be your name around the site.', max_length=10)),
                ('account_created', models.DateTimeField(verbose_name=b'account created')),
                ('school', models.CharField(default=b'Columbia', max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=16)),
                ('items', models.IntegerField(max_length=3)),
                ('photo', models.ImageField(upload_to=b'users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(to='traderbae.User'),
            preserve_default=True,
        ),
    ]
