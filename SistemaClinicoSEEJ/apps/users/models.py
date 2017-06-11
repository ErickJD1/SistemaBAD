# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Email debe ser obligatorio')
            email = self.normalize_email(email)
            user = self.model(username=username, email=email, is_active=True,
                              is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    def get_full_name(self):
        pass

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.URLField()

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # definicion de funciones
    def get_short_name(self):
        return self.username

class Permiso(model.models):
    descripcionPermiso = models.CharField(max_length=200)