# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Student

# Create your tests here.
class StudentTestCase(TestCase):

    def test_create_student(self):
        my_student = Student.objects.create_student(
            email='carlos@gmail.com',
            password='Pikachu32.',
            names='Carlos',
            lastnames='Barranco',
            identification_number='123456',
            phone='555-555-1',
            address='Av Venezuela Cardenalito',
            date_birth='2018-05-25')
        self.assertNotEqual(my_student, None)
        print "create student"
