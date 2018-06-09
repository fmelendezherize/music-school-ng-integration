# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db import IntegrityError
from .models import Professor
from .models import Subject, Department
from authentication.models import Profile

# Create your tests here.
class ProfessorTestCase(TestCase):
    '''
    Test Case for Professor
    '''
    def test_create_professor(self):
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        self.assertNotEqual(my_professor, None)
        self.assertEqual(my_professor.subjects.count(), 2)
        print "create professor"

    def test_create_duplicate_professor(self):
        try:
            department = Department.objects.create(name='Cuerdas')
            subject1 = Subject.objects.create(name='Cuatro', department=department)
            Professor.objects.create_professor(
                email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id])
            Professor.objects.create_professor(
                email='fmelendezherize@gmail.com', password='Pikachu12.', idsOfSubjects=[subject1.id])
            self.fail("Not Duplicate Professors Validation Fail")
        except IntegrityError:
            print "create duplicate professor"

    def test_get_professor_email_valid(self):
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id])
        get_professor = Professor.objects.get_professor_by_email('fmelendezherize@gmail.com')
        self.assertNotEqual(get_professor, None)
        print "get professor email valid"

    def test_get_professor_email_invalid(self):
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id])
        get_professor = Professor.objects.get_professor_by_email('wrongprofessor@gmail.com')
        self.assertEqual(get_professor, None)
        print "get professor email invalid"

    def test_check_professor_password(self):
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id])
        profile = Profile.objects.get(email='fmelendezherize@gmail.com')
        self.assertNotEqual(profile, None)
        self.assertEqual(profile.check_password('Pikachu32.'), True)
        print "check professor password"

    def test_register_professor(self):
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id])
        get_professor = Professor.objects.get_professor_by_email('fmelendezherize@gmail.com')
        self.assertNotEqual(get_professor, None)
        Professor.objects.register_professor(email='fmelendezherize@gmail.com', password='123456',
            names='Francisco A.', lastnames='Melendez Herize', identification_number='V13510355',
            phone='04127933553', address='Av 20 con Calle 19', skills='Tambor,Maracas')
        active_professor = Professor.objects.get_professor_by_email('fmelendezherize@gmail.com')
        self.assertEqual(active_professor.is_active, True)
        profile = Profile.objects.get(email='fmelendezherize@gmail.com')
        self.assertEqual(profile.check_password('123456'), True)
        print "register professor"        
