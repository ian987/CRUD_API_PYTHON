from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view() , name="book-list"), # for GET and POST
    path('books/<int:pk>/', BookList.as_view(), name="book-modify")# for PUT and DELETE
]