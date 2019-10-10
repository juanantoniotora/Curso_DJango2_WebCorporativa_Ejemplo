from django.db import models

# Create your models here.
class Author(models.Model):

    class Meta:
        db_table = 'authors'

class AbstractBook(models.Model):
    author = models.ForeignKey('books.Author', related_name='books')
    created_at = models.DateTimeField()

    class Meta:
        unmanaged = True
        abstract = True

class Book(Book):

    class Meta:
        db_table = 'books'

class HistoricBook(Book):

    class Meta:
        unmanaged = True
        db_table = 'books'
        app_label = 'historic'
