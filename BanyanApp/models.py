from __future__ import unicode_literals

import django
from django.db import models
from django.utils import *
from django.core.validators import MaxValueValidator, MinValueValidator

class Cat1(models.Model):
    num = 1 #identifier
    state1 = models.BooleanField(default=False)
    state2 = models.BooleanField(default=False)
    state3 = models.BooleanField(default=False)

    def __str__(self):
        return  "Category 1"

class Cat2(models.Model):
    num = 2 #identifier
    state1 = models.BooleanField(default=False)
    state2 = models.BooleanField(default=False)
    state3 = models.BooleanField(default=False)

    def __str__(self):
        return  "Category 2"

class Cat3(models.Model):
    num = 3 #identifier
    state1 = models.BooleanField(default=False)
    state2 = models.BooleanField(default=False)
    state3 = models.BooleanField(default=False)

    def __str__(self):
        return  "Category 3"

class Cat4(models.Model):
    num = 4 #identifier
    state1 = models.BooleanField(default=False)
    state2 = models.BooleanField(default=False)
    state3 = models.BooleanField(default=False)

    def __str__(self):
        return  "Category 4"

class Cat5(models.Model):
    num = 5 #identifier
    state1 = models.BooleanField(default=False)
    state2 = models.BooleanField(default=False)
    state3 = models.BooleanField(default=False)

    def __str__(self):
        return  "Category 5"

class Cat6(models.Model):
    num = 6 #identifier
    state1 = models.BooleanField(default=False)
    state2 = models.BooleanField(default=False)
    state3 = models.BooleanField(default=False)

    def __str__(self):
        return  "Category 6"
