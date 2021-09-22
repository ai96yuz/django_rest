from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/author', views.AuthorView)

urlpatterns = \
    [
        path('authors/', views.authors, name='authors'),
        path('<int:author_id>/', views.author_item, name='author_item'),
        path('create/', views.create_author, name='create_author'),
        path('delete/<int:pk>/', views.delete_author, name='delete_author'),
        path('update/<int:pk>/', views.update_author, name='update_author'),
        path('', include(router.urls))
    ]
