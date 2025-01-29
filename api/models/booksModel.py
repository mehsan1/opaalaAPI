from django.db import models
from api.models.listsModel import BookList


class BookRepository(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    year = models.IntegerField(blank=False, default='')
    name = models.CharField(max_length=70, blank=False, default='')
    list = models.ForeignKey(BookList, on_delete=models.DO_NOTHING, null=True)
    
objects = BookRepository()