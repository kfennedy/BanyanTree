from __future__ import unicode_literals

import django
from django.db import models
from django.utils import *
from django.core.validators import MaxValueValidator, MinValueValidator


class Light(models.Model):
    state = models.BooleanField(default=False)
    value = models.IntegerField(default=0, validators=[MaxValueValidator(100)])
    room = models.CharField(max_length=50)
    pin = models.IntegerField(default=0)

    def __str__(self):
        return  self.room  + "'s light"

class Air(models.Model):
    state = models.BooleanField(default=False)
    value = models.IntegerField(default=0, validators=[MinValueValidator(16), MaxValueValidator(30)])
    room = models.CharField(max_length=50)
    pin = models.IntegerField(default=0)

    def __str__(self):
        return  self.room  + "'s air"
