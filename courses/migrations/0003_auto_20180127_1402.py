# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-27 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0002_auto_20180127_1402'),
        ('students', '0002_auto_20180127_1402'),
        ('courses', '0002_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='department',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='block1',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='block2',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='places',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='professor_courses', to='professors.Professor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='students_enrolled',
            field=models.ManyToManyField(related_name='courses_enrolled', to='students.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='students_registered',
            field=models.ManyToManyField(related_name='courses_registered', to='students.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subject_courses', to='professors.Professor'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
