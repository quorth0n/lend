# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_auto_20171119_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.CharField(max_length=40),
        ),
    ]