# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 19:07
from __future__ import unicode_literals

from django.db import migrations, models
import monsters.models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0004_auto_20171218_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='attack',
            field=models.IntegerField(default=monsters.models.random_stats),
        ),
        migrations.AlterField(
            model_name='monster',
            name='defense',
            field=models.IntegerField(default=monsters.models.random_stats),
        ),
        migrations.AlterField(
            model_name='monster',
            name='health',
            field=models.IntegerField(default=monsters.models.random_stats),
        ),
        migrations.AlterField(
            model_name='monster',
            name='monster_type',
            field=models.CharField(default='Skeleton', max_length=100),
        ),
        migrations.AlterField(
            model_name='monster',
            name='name',
            field=models.CharField(default=monsters.models.random_name, max_length=30),
        ),
        migrations.AlterField(
            model_name='monster',
            name='unique_id',
            field=models.BigIntegerField(default=monsters.models.random_id),
        ),
    ]
