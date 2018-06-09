# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_deparment', to='professors.Department')),
            ],
        ),
        migrations.AlterField(
            model_name='professor',
            name='subjects',
            field=models.ManyToManyField(related_name='professor_subjects', to='professors.Subject'),
        ),
    ]
