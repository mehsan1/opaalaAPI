from injector  import inject
from api.models.listsModel import List

class ListService:
    @inject
    def __init__(self):
        self.message = "hello i am working fine"

    def get_lists(self):
        return List.objects.all()
    
    def get_list(self, id: int):
        return List.objects.get(id=id)
    
    def add_list(self, list: dict):
        _list = List()
        _list.title = list['title']
        return _list.save(_list)
    
    def update_list(self, list: dict):
        _list = self.get_list(list['id'])
        _list.title = list['title']
        return _list.save()
    
    def delete_list(self, list: dict):
        _list= self.get_list(list['id'])
        return _list.delete()