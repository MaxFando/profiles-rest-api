# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_auto_20180801_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='create_on',
            new_name='created_on',
        ),
    ]
