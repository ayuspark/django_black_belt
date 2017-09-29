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


class Friendship(models.Model):
    friend_to_add = models.ForeignKey(User, related_name='friend_to_add', default=None)
    user_who_requests = models.ForeignKey(User, related_name='user_who_requests', default=None)
    friendships = models.ManyToManyField(User, related_name='friendships')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

