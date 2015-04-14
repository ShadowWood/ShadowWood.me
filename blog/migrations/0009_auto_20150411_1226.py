# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_bloglist_read_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtext',
            name='article',
            field=models.OneToOneField(related_name=b'blog_text', to='blog.BlogList'),
        ),
    ]
