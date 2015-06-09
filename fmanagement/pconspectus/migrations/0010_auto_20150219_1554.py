# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pconspectus', '0009_cpaper_rpaper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpaper',
            old_name='title_connference',
            new_name='title_conference',
        ),
    ]
