from book.views import book_detail_view
from django.urls import path
from .views import AllOrdersCreated, book_by_user, home, AllOrdersPlated, HandOverBook
from . import views

urlpatterns = [
    path("", views.home, name='orders'),
    path("created/", AllOrdersCreated.as_view(), name='orders_created'),
    path("plated/", AllOrdersPlated.as_view(), name='orders_plated'),
    path("handover/",  HandOverBook.as_view(), name='hand_over_books'),
    path("user/111/", book_by_user, name = 'book_by_userId')
]
