from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.services.booksService import BookService
#from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from django.views import View
from injector import inject
from rest_framework.views import APIView
from api.dto.booksDTO import BooksDTO
# Create your views here.

class Books(APIView):
    @inject

    def __init__(self, bookservice: BookService):
        self.bookservice = bookservice
        super().__init__()

    #@api_view(['GET'])
    def get(self, request):
        if request.method == 'GET':
            books = self.bookservice.get_books()
            print(books)
            book_response = BooksDTO(books, many=True)
            return JsonResponse(book_response.data, safe=False)
            # 'safe=False' for objects serialization

    def bylist(self, request):
        if request.method == 'GET':
            
            books = self.bookservice.get_books()
            
            title = request.GET.get('title', None)
            if title is not None:
                tutorials = tutorials.filter(title__icontains=title)
            
            #tutorials_serializer = TutorialSerializer(tutorials, many=True)
            #return JsonResponse(tutorials_serializer.data, safe=False)
            # 'safe=False' for objects serialization