from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Author(models.Model):
    """

    """

    first_name = models.CharField(max_length=100,verbose_name='First Name')
    last_name = models.CharField(max_length=100,verbose_name='Last Name')

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Book(models.Model):
    """

    """

    author = models.ForeignKey(Author, related_name='books')
    title = models.CharField(max_length=200,verbose_name='Book Title')
    isbn = models.CharField(max_length=200, verbose_name='ISBN')

    def __unicode__(self):
        return self.title
