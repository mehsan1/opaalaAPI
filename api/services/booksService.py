from injector  import inject
from api.models.booksModel import Book

class BookService:
    @inject
    def __init__(self):
        self.message = "hello i am working fine"

    def get_books(self):
        return Book.objects.all()
        return "books are here"