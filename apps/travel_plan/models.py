# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


# Create your models here.
class TravelPlan(models.Model):
    creator = models.ForeignKey(User, related_name='plans')
    destination = models.CharField(max_length=25)
    desc = models.CharField(max_length=140, verbose_name='description')
    start_date = models.DateField(verbose_name='Travel Date From')
    end_date = models.DateField(verbose_name='Travel Date To')
    join = models.ManyToManyField(User, related_name='joined_plans')

    def __str__(self):
        plan = self.creator.username + ' ' + self.destination
        return plan
