from django.urls import path, include
from .views import *


urlpatterns = \
    [
        path('', books, name='books'),
        path('<int:book_id>/', book_item, name='book_item'),
        path('create/', create_book, name='create_book'),
        path('delete/<int:pk>/', delete_book, name='delete_book'),
        path('update/<int:pk>/', update_book, name='update_book'),
        path('book_search/', book_search, name='book_search'),
    ]

