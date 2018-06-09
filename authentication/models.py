# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.
class ProfileManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        account = self.model(
            email=self.normalize_email(email),
        )
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password=None):
        account = self.create_user(email=email, password=password)
        account.is_admin = True
        #Custom Role
        account.user_type = 'SU'
        account.save()
        return account

class Profile(AbstractBaseUser):
    type_account = (
        ('SU', 'Super User'),
        ('A', 'Admin'),
        ('P', 'Professor'),
        ('S', 'Students'),)

    user_type = models.CharField(max_length=2,
                                 choices=type_account,
                                 default='S')
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
  
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin