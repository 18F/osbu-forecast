# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='place_of_performance_city',
            field=models.CharField(max_length=100, default='Washington'),
        ),
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.CharField(blank=True, null=True, verbose_name='Product or Service Description', max_length=200),
        ),
    ]
