from django.db import models


class BookRepository(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    year = models.IntegerField(blank=False, default='')
    name = models.CharField(max_length=70, blank=False, default='')
    
objects = BookRepository()