# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150411_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='discuss',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.RemoveField(
            model_name='discuss',
            name='belong',
        ),
        migrations.DeleteModel(
            name='Discuss',
        ),
    ]
