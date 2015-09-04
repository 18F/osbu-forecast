# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0004_auto_20150904_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='osbu_advisor_phone',
            field=localflavor.us.models.PhoneNumberField(null=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='point_of_contat_phone',
            field=localflavor.us.models.PhoneNumberField(null=True, max_length=20, blank=True),
        ),
    ]
