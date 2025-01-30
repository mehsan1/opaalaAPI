from rest_framework import serializers 
from api.models.listsModel import List
 
 
class ListsDTO(serializers.ModelSerializer):
 
    class Meta:
        model = List
        fields = ('id',
                  'title')