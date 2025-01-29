from django.db import models
from booksModel import Book


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    year = models.IntegerField(blank=False, default='')
    name = models.CharField(max_length=70, blank=False, default='')
    list_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    