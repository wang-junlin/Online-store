# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-12-02 21:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191201_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='is_not',
            new_name='is_hot',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='is_now',
            new_name='is_new',
        ),
        migrations.RenameField(
            model_name='hotsearchwords',
            old_name='keyword',
            new_name='keywords',
        ),
    ]
