# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 13:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20160612_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobuser',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
