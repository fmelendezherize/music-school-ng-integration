# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-16 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_type', models.CharField(choices=[('SU', 'Super User'), ('A', 'Admin'), ('P', 'Professor'), ('S', 'Students')], default='S', max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
