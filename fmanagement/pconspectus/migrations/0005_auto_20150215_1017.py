# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0004_auto_20150214_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='second_author_fname',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='second_author_lname',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='second_author_middlename',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='third_author_fname',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='third_author_lname',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='third_author_middlename',
            field=models.CharField(null=True, blank=True, max_length=50),
            preserve_default=True,
        ),
    ]
