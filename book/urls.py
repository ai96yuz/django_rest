from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('api/v1/book', views.BookView)


urlpatterns = \
    [
        path('books/', views.books, name='books'),
        path('<int:book_id>/', views.book_item, name='book_item'),
        path('create/', views.create_book, name='create_book'),
        path('delete/<int:pk>/', views.delete_book, name='delete_book'),
        path('update/<int:pk>/', views.update_book, name='update_book'),
        path('book_search/', views.book_search, name='book_search'),
        path('', include(router.urls))
    ]

