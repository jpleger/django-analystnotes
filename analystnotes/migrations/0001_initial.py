# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cmd', models.CharField(max_length=2048, verbose_name=b'Command', db_index=True)),
                ('stdout', models.TextField(null=True, verbose_name=b'Standard Out', blank=True)),
                ('stderr', models.TextField(null=True, verbose_name=b'Standard Error', blank=True)),
                ('execute_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Process Execute Time')),
                ('exitcode', models.IntegerField(verbose_name=b'Process Exit Code', db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'Name of project', db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=128, verbose_name=b'Slug Name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Date project created', db_index=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='project',
            field=models.ForeignKey(to='analystnotes.Project'),
        ),
    ]
