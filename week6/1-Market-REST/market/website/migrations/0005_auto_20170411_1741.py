# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20170411_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('1', 'pending'), ('2', 'approved'), ('3', 'reject')], default='1', max_length=1),
        ),
    ]