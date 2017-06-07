# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20170606_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='coach_courses', to='coaches.Coach'),
            preserve_default=False,
        ),
    ]
