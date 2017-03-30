# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotebook', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='quotebook.User'),
        ),
    ]
