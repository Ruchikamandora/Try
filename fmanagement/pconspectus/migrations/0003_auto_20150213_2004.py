# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='Mrs', choices=[('Dr.', 'Dr.'), ('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], max_length=50),
            preserve_default=True,
        ),
    ]
