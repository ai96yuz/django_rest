from django.urls import path, include
from . import views
from .views import *

urlpatterns = \
    [
        path('', views.users, name='users'),
        path('<int:user_id>/', views.user_item, name='user_item'),
        path('delete/<int:user_id>/', views.delete_user),
        path('signup/', views.register, name="create_user"),
        path('signup/<int:user_id>/', views.update_user, name="update_user"),
        path('api/v1/user/', UserListCreate.as_view()),
        path('api/v1/user/<int:pk>/', UserViewUpdateDelete.as_view()),
        path('api/v1/user/<int:user_pk>/order/', OrdersListForUser.as_view()),
    ]
