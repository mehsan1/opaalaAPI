from rest_framework import serializers
from api.dto.listsDTO import ListsDTO
from api.models.booksModel import Book


class BooksDTO(serializers.ModelSerializer):
    class Meta:
        list_id = ListsDTO(read_only=True)

        model = Book
        fields = ("id", "title", "year", "name", "list_id")
