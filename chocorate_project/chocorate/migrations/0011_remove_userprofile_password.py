# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-23 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chocorate', '0010_auto_20180323_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]
