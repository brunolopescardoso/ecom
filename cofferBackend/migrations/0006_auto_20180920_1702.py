# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-20 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cofferBackend', '0005_auto_20180920_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dt_nasc',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data Nascimento'),
        ),
    ]
