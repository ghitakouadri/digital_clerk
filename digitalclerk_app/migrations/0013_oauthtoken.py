# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-05 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalclerk_app', '0012_auto_20171125_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=80)),
            ],
        ),
    ]
