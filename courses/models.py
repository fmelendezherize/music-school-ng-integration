# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from students.models import Student
from professors.models import Professor, Subject

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    places = models.IntegerField(default=25)
    professor = models.ForeignKey(Professor, related_name='professor_courses')
    subject = models.ForeignKey(Subject, related_name='subject_courses')
    block1 = models.CharField(max_length=2)
    block2 = models.CharField(max_length=2)
    students_registered = models.ManyToManyField(Student, related_name='courses_registered')
    students_enrolled = models.ManyToManyField(Student, related_name='courses_enrolled')

    def register_student(self, student):
        #Validate that is not already registered here
        if self.students_registered.filter(pk=student.id).exists():
            raise ValueError("Student already registered")
        if self.students_enrolled.filter(pk=student.id).exists():
            raise ValueError("Student already registered")
        #Validate that the student is not registered on the same time block
        if student.courses_registered.filter(block1=self.block1).exists() or \
            student.courses_enrolled.filter(block1=self.block1).exists():
            raise ValueError("The Student has already ocuppied this block with another course")
        if student.courses_registered.filter(block2=self.block2).exists() or \
            student.courses_enrolled.filter(block2=self.block2).exists():
            raise ValueError("The Student has already ocuppied this block with another course")
        #Regiser
        self.students_registered.add(student)
        if self.places == 0:
            raise ValueError("No more places in course. Sorry")
        #Insert a pending student and decrease places
        self.places = self.places - 1
    
    def enroll_student(self, idStudent):
        #Approve a student
        student = self.students_registered.get(pk=idStudent)
        self.students_registered.remove(student)
        self.students_enrolled.add(student)

    def reject_student(self, idStudent):
        #Remove student and increace places
        student = self.students_registered.get(pk=idStudent)
        self.students_registered.remove(student)
        self.places = self.places + 1

    def __unicode__(self):
        return self.name
    