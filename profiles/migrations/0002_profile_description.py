# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
