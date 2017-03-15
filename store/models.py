from __future__ import unicode_literals


from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('users.User')
    books = models.ManyToManyField('library.Book')
