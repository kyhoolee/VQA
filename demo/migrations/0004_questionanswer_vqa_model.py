# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-06-03 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20170511_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='vqa_model',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
