from injector  import inject
from api.models.listsModel import List

class ListService:
    @inject
    def __init__(self):
        self.message = "hello i am working fine"

    def get_lists(self):
        return List.objects.all()
        return "books are here"