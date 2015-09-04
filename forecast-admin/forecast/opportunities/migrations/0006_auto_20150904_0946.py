# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0005_auto_20150904_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='osbu_advisor_email',
            field=models.EmailField(null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='point_of_contact_email',
            field=models.EmailField(null=True, max_length=200, blank=True),
        ),
    ]
