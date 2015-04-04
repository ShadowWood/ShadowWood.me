# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150331_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloglist',
            old_name='keyword1',
            new_name='keywords',
        ),
        migrations.RemoveField(
            model_name='bloglist',
            name='keyword2',
        ),
        migrations.RemoveField(
            model_name='bloglist',
            name='keyword3',
        ),
        migrations.RemoveField(
            model_name='bloglist',
            name='keyword4',
        ),
    ]
