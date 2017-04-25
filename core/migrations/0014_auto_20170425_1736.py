# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170425_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='authorize_photo',
            field=models.TextField(blank=True, default='', verbose_name='Autoriza foto'),
        ),
        migrations.AddField(
            model_name='recipient',
            name='estudies',
            field=models.TextField(blank=True, default='', verbose_name='Estudios'),
        ),
        migrations.AddField(
            model_name='recipient',
            name='sibling',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Hermanos'),
        ),
    ]