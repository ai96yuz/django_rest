from django.urls import path, include
from . import views


urlpatterns = \
    [
        path('authors/', views.authors, name='authors'),
        path('authors/<int:author_id>/', views.author_item, name='author_item'),
        path('authors/create/', views.create_author, name='create_author'),
        path('authors/delete/<int:pk>/', views.delete_author, name='delete_author'),
        path('authors/update/<int:pk>/', views.update_author, name='update_author'),
    ]