# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


# Register your models here.

class UserAdmin(UserAdmin):

    fieldsets = (
        ('User', {'fields': ('username', 'password')}),

        ('Personal_Info', {'fields': ('first_name',
                                      'last_name',
                                      'email',
                                      'avatar')}),

        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions',
                                    )}),
    )
    # list_display = ('username', 'email','avatar', 'first_name', 'last_name',
    #                 'is_active', 'is_staff','is_superuser', 'location')

    # def __init__(self):
    #     pass
    #

admin.site.register(User, UserAdmin)
