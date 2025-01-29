from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
#from tutorials.models import Tutorial
#from tutorials.serializers import TutorialSerializer
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def list(request):
    if request.method == 'GET':
        return JsonResponse(["heloo i am working..."], safe=False)
        tutorials = Tutorial.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization