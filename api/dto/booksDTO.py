from rest_framework import serializers 
from api.models.booksModel import Book
 
 
class BooksDTO(serializers.ModelSerializer):
 
    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'year',
                  'name',
                  'list_id')