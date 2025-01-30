from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.services.listsService import ListService
#from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from django.views import View
from injector import inject
from rest_framework.views import APIView
from api.dto.listsDTO import ListsDTO
# Create your views here.

class Lists(APIView):
    @inject

    def __init__(self, listService: ListService):
        self.listService = listService
        super().__init__()

    #@api_view(['GET'])
    def get(self, request):
        if request.method == 'GET':
            books = self.listService.get_lists()
            book_response = ListsDTO(books, many=True)
            return JsonResponse({"success":"true", "results":book_response.data}, safe=False)
            # 'safe=False' for objects serialization

    
        if request.method == 'GET':
            
            books = self.bookservice.get_books()
            
            title = request.GET.get('title', None)
            if title is not None:
                tutorials = tutorials.filter(title__icontains=title)
            
            #tutorials_serializer = TutorialSerializer(tutorials, many=True)
            #return JsonResponse(tutorials_serializer.data, safe=False)
            # 'safe=False' for objects serialization