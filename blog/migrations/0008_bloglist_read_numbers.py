# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150401_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglist',
            name='read_numbers',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=True,
        ),
    ]
