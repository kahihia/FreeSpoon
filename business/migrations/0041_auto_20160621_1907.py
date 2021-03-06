# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0040_auto_20160621_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='cover',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image'),
        ),
        migrations.AddField(
            model_name='dishdetails',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cover',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image'),
        ),
        migrations.AddField(
            model_name='step',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Image'),
        ),
    ]
