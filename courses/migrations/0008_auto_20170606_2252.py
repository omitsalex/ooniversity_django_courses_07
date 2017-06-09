# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-06 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170603_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_courses', to='coaches.Coach'),
        ),
    ]