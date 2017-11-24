# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webterminal', '0010_commandssequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servergroup',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name=b'Server group name'),
        ),
        migrations.AlterField(
            model_name='serverinfor',
            name='ip',
            field=models.GenericIPAddressField(protocol=b'ipv4'),
        ),
        migrations.AlterField(
            model_name='serverinfor',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name=b'Server name'),
        ),
    ]
