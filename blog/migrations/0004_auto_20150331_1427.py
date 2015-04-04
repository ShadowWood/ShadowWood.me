# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141127_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(max_length=10)),
                ('title', models.CharField(max_length=20)),
                ('introduction', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_body', models.TextField()),
                ('article', models.ForeignKey(to='blog.BlogList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_id', models.IntegerField(max_length=2)),
                ('type_name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('belong', models.ForeignKey(related_name=b'content', to='blog.BlogList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='blog_list',
        ),
        migrations.DeleteModel(
            name='blog_text',
        ),
        migrations.AddField(
            model_name='bloglist',
            name='type',
            field=models.ForeignKey(to='blog.BlogType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='discuss',
            field=models.ForeignKey(to='blog.Discuss'),
            preserve_default=True,
        ),
    ]
