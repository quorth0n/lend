# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=20)),
                ('age', models.SmallIntegerField()),
            ],
        ),
    ]