# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webterminal', '0008_auto_20170921_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name=b'Credential name'),
        ),
    ]
