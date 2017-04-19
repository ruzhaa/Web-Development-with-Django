# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20170419_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='website.Category'),
        ),
    ]
