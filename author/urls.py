from django.urls import path
from .views import *

urlpatterns = [
    path("", AuthorListView.as_view(), name='authors'),
    path('<int:author_id>/', author_detail_view, name="author_details"),
]