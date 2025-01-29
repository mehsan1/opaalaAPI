from django.db import models

class BookList(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')