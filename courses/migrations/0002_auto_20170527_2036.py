# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-27 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]