# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170425_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='comment',
            field=models.TextField(blank=True, default='', verbose_name='Observaciones'),
        ),
    ]
