from django.urls import path, include
from .views import *


urlpatterns = [
    path("", all_books_view, name='books'),
    path("<int:book_id>/", book_detail_view, name="book_details"),
    path("unordered/", UnorderedBookListView.as_view(), name="unordered"),
    path("books/", book_search, name="search_box"),
    path('asc/', sort_book_asc, name="sort_book_asc"),
    path('desc/', sort_book_desc, name="sort_book_desc"),
    path('count/', sort_book_count, name="sort_book_count")
]
