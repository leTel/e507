# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('message', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('language', models.CharField(max_length=20, choices=[('fr', 'French'), ('en', 'English'), ('de', 'German')])),
            ],
        ),
    ]
