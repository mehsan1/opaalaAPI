from django.db import models
from api.models.listsModel import List
from api.models.booksModel import Book


class ListBooksRepository(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class ListBooks(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True)
    list = models.ForeignKey(List, on_delete=models.DO_NOTHING, null=True)


objects = ListBooksRepository()
