# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0054_product_tag_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulk',
            name='seq',
            field=models.IntegerField(default=0, max_length=11),
        ),
    ]