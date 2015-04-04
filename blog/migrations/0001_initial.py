# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_list',
            fields=[
                ('article_id', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=10)),
                ('introduction', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='blog_text',
            fields=[
                ('article_id', models.IntegerField(serialize=False, primary_key=True)),
                ('article_body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
