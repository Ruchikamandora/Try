# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0006_auto_20150215_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='first_author_middlename',
        ),
        migrations.RemoveField(
            model_name='book',
            name='second_author_middlename',
        ),
        migrations.RemoveField(
            model_name='book',
            name='third_author_middlename',
        ),
        migrations.AddField(
            model_name='book',
            name='citation',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
    ]
