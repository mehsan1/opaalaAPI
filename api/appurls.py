
from api.controller.Books import  Books
from django.urls import include, path, re_path

 
urlpatterns = [ 
    path('books',Books.as_view(), name='index')
    #re_path(r'^api/books$', Books.list)
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]