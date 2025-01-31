
from api.controller.Books import  Books
from api.controller.Lists import  Lists
from django.urls import path

 
urlpatterns = [ 
    path('books',Books.as_view(), name='index'),
    path('lists', Lists.as_view(), name='')
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]