# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numplate', '0004_auto_20170216_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carplate',
            name='outTime',
            field=models.DateTimeField(default=None),
        ),
    ]
