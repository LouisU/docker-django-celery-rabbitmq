# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-17 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0007_auto_20170117_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='result',
            field=models.TextField(default=b'None'),
        ),
    ]
