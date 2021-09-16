from django.urls import path
from .views import *

urlpatterns = [
    path("", UserListView.as_view(), name='users'),
    path('<int:user_id>/', user_detail_view, name="user_details"),
]
