# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    birthday = models.DateField()


class Friend(models.Model):
    # friend = models.CharField(max_length=12)
    friend_username = models.OneToOneField(User, related_name='friend')


class Friendship(models.Model):
    friendship = models.ManyToManyField(User, related_name='fs')
