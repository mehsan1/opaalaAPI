from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.services.listsService import ListService

# from tutorials.serializers import TutorialSerializer
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

    # @api_view(['GET'])
    def get(self, request):
        if request.method == "GET":
            lists = self.listService.get_lists()
            list_response = ListsDTO(lists, many=True)
            return JsonResponse(
                {"success": "true", "results": list_response.data}, safe=False
            )

    def post(self, request):
        if request.method == "POST":
            self.listService.add_list(request.data)
            return JsonResponse({"success": "true", "results": []}, safe=False)

    def put(self, request):
        if request.method == "PUT":
            self.listService.update_list(request.data)
            return JsonResponse({"success": "true", "results": []}, safe=False)

    def delete(self, request):
        if request.method == "DELETE":
            self.listService.delete_list(request.data)
            return JsonResponse({"success": "true", "results": []}, safe=False)
