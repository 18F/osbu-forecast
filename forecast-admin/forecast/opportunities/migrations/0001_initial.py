# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('award_status', models.CharField(choices=[('Pending', 'Award Pending'), ('Awarded', 'Awarded')], max_length=50)),
                ('description', models.CharField(verbose_name='Product or Service Description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('organization', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=30)),
            ],
        ),
    ]
