# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150401_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtext',
            name='article',
            field=models.OneToOneField(to='blog.BlogList'),
        ),
    ]
