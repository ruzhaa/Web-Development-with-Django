# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170314_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.Tags'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]