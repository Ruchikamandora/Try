# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pconspectus.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('full_name', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('designation', models.CharField(max_length=50, blank=True)),
                ('picture', models.FileField(upload_to=pconspectus.models.get_upload_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
