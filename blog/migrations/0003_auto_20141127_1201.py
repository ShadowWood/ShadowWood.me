# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141127_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_list',
            name='article_id',
            field=models.CharField(max_length=3, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='blog_text',
            name='article_id',
            field=models.CharField(max_length=3, serialize=False, primary_key=True),
        ),
    ]
