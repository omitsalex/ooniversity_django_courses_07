# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=255)),
                ('skype', models.CharField(max_length=32)),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
        ),
    ]