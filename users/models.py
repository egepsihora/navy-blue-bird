from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser


@python_2_unicode_compatible
class User(AbstractUser):
    birthDate = models.DateField(null=True, blank=True)
    index = models.IntegerField(null=True)
    country = models.CharField(max_length=50, blank=True, default='')
    city = models.CharField(max_length=20, blank=True, default='')
    street = models.CharField(max_length=40, blank=True, default='')
    house = models.IntegerField(null=True)
    apartments = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.username
