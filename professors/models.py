# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

#from courses.models import Subject
from authentication.models import Profile

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    department = models.ForeignKey(Department, related_name='subject_deparment', on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.id) + ":" + self.name

class ProfessorManager(models.Manager):
    '''
    Custom Professor Manager
    '''
    def create_professor(self, email, password, idsOfSubjects):
        '''
        This action is made by the admin user. Create Professor with a mininum data.
        '''
        #Validate Subjects
        if len(idsOfSubjects) < 1:
            raise ValueError("Ids of Subjects invalid.")
        listOfSubjects = []
        for subjectid in idsOfSubjects:
            try:
                subject = Subject.objects.get(id=subjectid)
            except Subject.DoesNotExist:
                raise ValueError("Ids of Subjects invalid.")
            listOfSubjects.append(subject)
        #Create Profile
        new_profile = Profile.objects.create_user(email=email, password=password)
        new_profile.user_type = 'P'
        new_profile.save()
        #Create Professor
        new_professor = Professor.objects.create(user=new_profile)
        for subject in listOfSubjects:
            new_professor.subjects.add(subject)
        new_professor.save()
        return new_professor

    def register_professor(self, email, password, **kwargs):
        '''
        This action is made by the professor user. Complete the profile data.
        '''
        professor = self.get_professor_by_email(email)
        if professor is None:
            raise ValueError("email is invalid.")
        account = professor.user
        #Necesitamos validar la password :/
        account.set_password(password)
        professor.names = kwargs['names']
        professor.lastnames = kwargs['lastnames']
        professor.identification_number = kwargs['identification_number']
        professor.phone = kwargs['phone']
        professor.address = kwargs['address']
        professor.skills = kwargs['skills']
        professor.is_active = True
        account.save()
        professor.save()
        return professor

    def get_professor_by_email(self, email):
        return Professor.objects.filter(user__email=email).first()

class Professor(models.Model):
    '''
    Professor Class
    '''
    names = models.CharField(max_length=200, null=True, blank=True)
    lastnames = models.CharField(max_length=200, null=True, blank=True)
    identification_number = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='professor_subjects')
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    objects = ProfessorManager()

    def __unicode__(self):
        return str(self.id)
