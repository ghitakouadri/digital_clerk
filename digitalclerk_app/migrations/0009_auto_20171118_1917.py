# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-18 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalclerk_app', '0008_interaction_duration_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.IntegerField(choices=[(2, 'Pending'), (1, 'Open'), (0, 'Closed')], default=1),
        ),
    ]
