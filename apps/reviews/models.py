# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        name = self.first_name.title() + ' ' + self.last_name.title()
        return name

class Book(models.Model):
    title = models.CharField(max_length=140)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title
    

class Review(models.Model):
    rating = models.PositiveIntegerField(default=5, 
                                         validators=(MinValueValidator(1),
                                                     MaxValueValidator(5))
                                        )
    comment = models.TextField(max_length=140)
    user = models.ForeignKey(User, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.comment
    
    def update(self):
        self.update_date = timezone.now
        self.save()


