from rest_framework import serializers 
from api.models.listBooksModel import ListBooks
 
 
class listsBookDTO(serializers.ModelSerializer):
 
    class Meta:
        model = ListBooks
        fields = ('id',
                  'title')