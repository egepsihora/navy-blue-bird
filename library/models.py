from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info = models.TextField(blank=True, default='')
    books = models.ManyToManyField('Book')

    @property
    def full_name(self):
        return self.name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    commentator = models.ForeignKey('users.User',
                                    on_delete=models.SET('Anonymous'))
    book = models.ForeignKey('Book', on_delete=models.CASCADE)






