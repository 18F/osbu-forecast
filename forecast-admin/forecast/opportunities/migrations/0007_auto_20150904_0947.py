# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0006_auto_20150904_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='estimated_solicitation_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
