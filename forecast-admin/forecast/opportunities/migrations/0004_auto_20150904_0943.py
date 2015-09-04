# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0003_award_place_of_performance_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='additional_information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='competition_strategy',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='delivery_order_value',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='estimated_fiscal_year',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='estimated_fiscal_year_quarter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='estimated_solicitation_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='fedbizopps_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='funding_agency',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='incumbent_name',
            field=models.CharField(blank=True, verbose_name='Incumbent Contractor Name', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='naics',
            field=models.CharField(blank=True, verbose_name='Primary NAICS Code', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='new_requirement',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='osbu_advisor_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='osbu_advisor_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='osbu_advisor_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='point_of_contact_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='point_of_contact_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='point_of_contat_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='price_max',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='price_min',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='procurement_method',
            field=models.CharField(blank=True, verbose_name='Procurement Method', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='award',
            name='socioeconomic',
            field=models.CharField(blank=True, verbose_name='Socioeconomic Category', max_length=50, null=True),
        ),
    ]
