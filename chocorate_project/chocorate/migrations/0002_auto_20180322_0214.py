# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocorate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='avgrating',
            field=models.FloatField(),
        ),
    ]