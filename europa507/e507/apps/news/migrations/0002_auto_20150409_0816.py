# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='language',
            field=models.CharField(choices=[('fr', 'French'), ('en', 'English'), ('de', 'German')], max_length=20, default='fr'),
        ),
    ]
