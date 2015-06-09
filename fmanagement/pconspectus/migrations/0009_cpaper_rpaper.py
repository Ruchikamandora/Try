# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pconspectus.models


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0008_bookchapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cpaper',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title_paper', models.CharField(max_length=500, blank=True)),
                ('title_connference', models.CharField(max_length=500, blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('publication_year', models.CharField(max_length=50)),
                ('pages', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('publication_place', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=500, blank=True)),
                ('title_first', models.CharField(default='Mrs', max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')])),
                ('first_author_fname', models.CharField(max_length=50)),
                ('first_author_lname', models.CharField(max_length=50)),
                ('title_second', models.CharField(default='Mrs', max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')])),
                ('second_author_fname', models.CharField(max_length=50, blank=True, null=True)),
                ('second_author_lname', models.CharField(max_length=50, blank=True, null=True)),
                ('title_third', models.CharField(default='Mrs', max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')])),
                ('third_author_fname', models.CharField(max_length=50, blank=True, null=True)),
                ('third_author_lname', models.CharField(max_length=50, blank=True, null=True)),
                ('file', models.FileField(upload_to=pconspectus.models.get_upload_file_name)),
                ('citation', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rpaper',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=500, blank=True)),
                ('abstract', models.TextField(blank=True)),
                ('publication_year', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('title_first', models.CharField(default='Mrs', max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')])),
                ('first_author_fname', models.CharField(max_length=50)),
                ('first_author_lname', models.CharField(max_length=50)),
                ('title_second', models.CharField(default='Mrs', max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')])),
                ('second_author_fname', models.CharField(max_length=50, blank=True, null=True)),
                ('second_author_lname', models.CharField(max_length=50, blank=True, null=True)),
                ('title_third', models.CharField(default='Mrs', max_length=50, choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')])),
                ('third_author_fname', models.CharField(max_length=50, blank=True, null=True)),
                ('third_author_lname', models.CharField(max_length=50, blank=True, null=True)),
                ('file', models.FileField(upload_to=pconspectus.models.get_upload_file_name)),
                ('citation', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
