# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BanyanApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='air',
            name='pin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='light',
            name='pin',
            field=models.IntegerField(default=0),
        ),
    ]
