# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0009_auto_20160525_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_wechat',
            field=models.CharField(max_length=200),
        ),
    ]