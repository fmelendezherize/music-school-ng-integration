# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Course
from professors.models import Department, Subject, Professor
from students.models import Student

# Create your tests here.
class CoursesTestCase(TestCase):

    def test_create_course(self):
        print "create course"
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        my_course = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1, block1='M1', block2='W5')
        self.assertEqual(Course.objects.count(), 1)        

    def test_enroll_student_course(self):
        print "enroll student"
        #Define department, Subjects
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        #Define Professor
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        #Define Course
        my_course = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1)
        #Define Student
        my_student = Student.objects.create_student(
            email='carlos@gmail.com',
            password='Pikachu32.',
            names='Carlos',
            lastnames='Barranco',
            identification_number='123456',
            phone='555-555-1',
            address='Av Venezuela Cardenalito',
            date_birth='2018-05-25')
        #Register Student
        my_course.register_student(my_student)
        my_course.save()
        self.assertEqual(my_course.students_registered.count(), 1)
        self.assertEqual(my_course.places, 24)
        #Test Persistence
        the_course = Course.objects.get(pk=my_course.id)
        self.assertNotEqual(the_course, None)
        self.assertEqual(the_course.students_registered.count(), 1)        
        self.assertEqual(the_course.places, 24)        

    def test_assign_professor_courses(self):
        print "assign professor to courses"
        #Define department, Subjects
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        #Define Professor
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        #Define Course
        course1 = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1)
        course2 = Course.objects.create(name='curso de violin italiano', professor=my_professor,
            subject=subject2)
        the_professor = Professor.objects.get(pk=my_professor.id)
        self.assertNotEqual(the_professor, None)
        self.assertEqual(the_professor.professor_courses.count(), 2)        

    def test_student_register_to_course(self):
        print "register student to course"
        #Define department, Subjects
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        #Define Professor
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        #Define Course
        course1 = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1)
        course2 = Course.objects.create(name='curso de violin italiano', professor=my_professor,
            subject=subject2)
        #Define Student
        my_student = Student.objects.create_student(
            email='carlos@gmail.com',
            password='Pikachu32.',
            names='Carlos',
            lastnames='Barranco',
            identification_number='123456',
            phone='555-555-1',
            address='Av Venezuela Cardenalito',
            date_birth='2018-05-25')
        #Register Student
        course1.register_student(my_student)
        course1.save()
        #Relations
        the_student = Student.objects.get(pk=my_student.id)
        self.assertNotEqual(the_student, None)
        self.assertEqual(the_student.courses_registered.count(), 1)        

    def test_student_enrollment_to_course(self):
        print "enroll student to course"
        #Define department, Subjects
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        #Define Professor
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        #Define Course
        course1 = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1)
        #Define Student
        my_student = Student.objects.create_student(
            email='carlos@gmail.com',
            password='Pikachu32.',
            names='Carlos',
            lastnames='Barranco',
            identification_number='123456',
            phone='555-555-1',
            address='Av Venezuela Cardenalito',
            date_birth='2018-05-25')
        #Register Student
        course1.register_student(my_student)
        course1.save()
        #Enroll Student
        course1.enroll_student(my_student.id)
        the_student = Student.objects.get(pk=my_student.id)
        self.assertEqual(the_student.courses_registered.count(), 0)
        self.assertEqual(the_student.courses_enrolled.count(), 1)

    def test_student_already_register_in_course(self):
        print "register student to course twice"
        #Define department, Subjects
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        #Define Professor
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        #Define Course
        course1 = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1)
        #Define Student
        my_student = Student.objects.create_student(
            email='carlos@gmail.com',
            password='Pikachu32.',
            names='Carlos',
            lastnames='Barranco',
            identification_number='123456',
            phone='555-555-1',
            address='Av Venezuela Cardenalito',
            date_birth='2018-05-25')
        #Register Student
        course1.register_student(my_student)
        course1.save()
        #Register Again
        try:           
            course1.register_student(my_student)
            self.fail("Not duplicate Student in register Validation Fail")
        except ValueError:
            pass

    def test_student_register_in_ocuppied_course_block(self):
        print "register student to in ocuppied course block"
        #Define department, Subjects
        department = Department.objects.create(name='Cuerdas')
        subject1 = Subject.objects.create(name='Cuatro', department=department)
        subject2 = Subject.objects.create(name='Violin', department=department)
        #Define Professor
        my_professor = Professor.objects.create_professor(
            email='fmelendezherize@gmail.com', password='Pikachu32.', idsOfSubjects=[subject1.id, subject2.id])
        #Define Course 1
        course1 = Course.objects.create(name='curso de cuatro venezolano', professor=my_professor,
            subject=subject1, block1='M2', block2='W3')
        #Define Course 2
        course2 = Course.objects.create(name='curso de violin larense', professor=my_professor,
            subject=subject1, block1='M2', block2='X3')
        #Define Student
        my_student = Student.objects.create_student(
            email='carlos@gmail.com',
            password='Pikachu32.',
            names='Carlos',
            lastnames='Barranco',
            identification_number='123456',
            phone='555-555-1',
            address='Av Venezuela Cardenalito',
            date_birth='2018-05-25')
        try:            
            #Register Student
            course1.register_student(my_student)
            course1.save()
            #Validation error
            course2.register_student(my_student)
            self.fail("Student ocuppied block Validation Fail")
        except ValueError:
            pass

        #Test Reject Student
        #Test Course Full

