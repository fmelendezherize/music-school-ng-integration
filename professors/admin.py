# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Professor
from .models import Department, Subject

# Register your models here.
admin.site.register(Professor)
admin.site.register(Department)
admin.site.register(Subject)
