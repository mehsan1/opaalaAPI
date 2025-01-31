from django.db import models


class ListRepository(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class List(models.Model):
    title = models.CharField(max_length=70, blank=False, default="")


objects = ListRepository()
