# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0007_auto_20150904_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='point_of_contat_phone',
            new_name='point_of_contact_phone',
        ),
    ]
