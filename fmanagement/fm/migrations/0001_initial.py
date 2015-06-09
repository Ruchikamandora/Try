# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('full_name', models.CharField(primary_key=True, max_length=40, serialize=False)),
                ('contactno', models.IntegerField(blank=True, max_length=10)),
                ('academic_qualifiacation', models.TextField(blank=True)),
                ('experience', models.TextField(blank=True)),
                ('subjects_profeciencies', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
