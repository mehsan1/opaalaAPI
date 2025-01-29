from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    year = models.IntegerField(blank=False, default='')
    name = models.CharField(max_length=70, blank=False, default='')
    list_id = models.IntegerField(blank=False, default=0)

class BookList(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')