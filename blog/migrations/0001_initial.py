# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 05:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('publish_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Topic'),
        ),
    ]