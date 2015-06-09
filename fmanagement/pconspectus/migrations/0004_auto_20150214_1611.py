# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0003_auto_20150213_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='title_first',
        ),
        migrations.AddField(
            model_name='book',
            name='title_second',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], max_length=50, default='Mrs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='title_third',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], max_length=50, default='Mrs'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
