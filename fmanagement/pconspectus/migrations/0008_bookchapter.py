# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pconspectus.models


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0007_auto_20150215_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title_chapter', models.CharField(max_length=500, blank=True)),
                ('title_book', models.CharField(max_length=500, blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('publication_year', models.CharField(max_length=50)),
                ('pages', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=500, blank=True)),
                ('title_first', models.CharField(max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], default='Mrs')),
                ('first_author_fname', models.CharField(max_length=50)),
                ('first_author_lname', models.CharField(max_length=50)),
                ('title_second', models.CharField(max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], default='Mrs')),
                ('second_author_fname', models.CharField(max_length=50, null=True, blank=True)),
                ('second_author_lname', models.CharField(max_length=50, null=True, blank=True)),
                ('title_third', models.CharField(max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], default='Mrs')),
                ('third_author_fname', models.CharField(max_length=50, null=True, blank=True)),
                ('third_author_lname', models.CharField(max_length=50, null=True, blank=True)),
                ('file', models.FileField(upload_to=pconspectus.models.get_upload_file_name)),
                ('citation', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
