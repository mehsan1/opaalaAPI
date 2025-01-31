from django.http.response import JsonResponse
from api.models.booksModel import Book
from api.services.booksService import BookService
from injector import inject
from rest_framework.views import APIView
from api.dto.booksDTO import BooksDTO


class Books(APIView):
    @inject
    def __init__(self, bookservice: BookService):
        self.bookservice = bookservice
        super().__init__()

    # @api_view(['GET'])
    def get(self, request):
        if request.method == "GET":
            try:
                books = self.bookservice.get_books()
                book_response = BooksDTO(books, many=True)
            except books.DoesNotExist:
                return JsonResponse({"success": "false", "results": []})

            return JsonResponse(
                {"success": "true", "results": book_response.data}, safe=False
            )

            # 'safe=False' for objects serialization

    def post(self, request):
        if request.method == "POST":
            self.bookservice.add_book(request.data)
            return JsonResponse({"success": "true", "results": []}, safe=False)

    def put(self, request):
        if request.method == "PUT":
            self.bookservice.update_book(request.data)
            return JsonResponse({"success": "true", "results": []}, safe=False)

    def delete(self, request):
        if request.method == "DELETE":
            self.bookservice.delete_book(request.data)
            return JsonResponse({"success": "true", "results": []}, safe=False)
