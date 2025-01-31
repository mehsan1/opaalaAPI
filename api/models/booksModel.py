from django.db import models
from api.models.listsModel import List

class BookRepository(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_by_id(self, _id: int):
        return super().get_queryset().filter(id=_id)


class Meta:
    db_table = "book"


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default="")
    year = models.IntegerField(blank=False, default="")
    name = models.CharField(max_length=70, blank=False, default="")
    list = models.ForeignKey(
        List, related_name="Book", blank=True, null=True, on_delete=models.DO_NOTHING
    )


objects = BookRepository()
