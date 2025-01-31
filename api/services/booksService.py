from injector import inject
from api.models.booksModel import Book
from api.models.listsModel import List


class BookService:
    @inject
    def __init__(self):
        self.message = "hello i am working fine"

    def get_books(self):
        return Book.objects.all()
        return "books are here"

    def get_book(self, id: int):
        return Book.objects.get(id=id)

    def add_book(self, book: dict):
        _book = Book()
        _book.title = book["title"]
        _book.name = book["name"]
        _book.year = book["year"]
        if book["list_id"] and book["list_id"] != "" and int(book["list_id"]) > 0:
            _list = List(book["list_id"])
            _book.list = _list  

        return _book.save(_book)

    def update_book(self, book: dict):
        _book = self.get_book(book["id"])
        _book.title = book["title"]
        _book.name = book["name"]
        _book.year = book["year"]
        if book["list_id"] and book["list_id"] != "" and int(book["list_id"]) > 0:
            _list = List(book["list_id"])
            _book.list = _list
        return _book.save()

    def delete_book(self, book: dict):
        _book = self.get_book(book["id"])
        return _book.delete()
