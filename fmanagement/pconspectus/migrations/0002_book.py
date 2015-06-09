# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pconspectus.models


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField(blank=True)),
                ('publication_year', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('first_author_fname', models.CharField(max_length=50)),
                ('first_author_middlename', models.CharField(blank=True, max_length=50)),
                ('first_author_lname', models.CharField(max_length=50)),
                ('second_author_fname', models.CharField(blank=True, max_length=50)),
                ('second_author_middlename', models.CharField(blank=True, max_length=50)),
                ('second_author_lname', models.CharField(blank=True, max_length=50)),
                ('third_author_fname', models.CharField(blank=True, max_length=50)),
                ('third_author_middlename', models.CharField(blank=True, max_length=50)),
                ('third_author_lname', models.CharField(blank=True, max_length=50)),
                ('file', models.FileField(upload_to=pconspectus.models.get_upload_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
