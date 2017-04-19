# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 19:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20170411_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]