# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocorate', '0009_chocolate_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='picture_url',
            field=models.CharField(max_length=200),
        ),
    ]
