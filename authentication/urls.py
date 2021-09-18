from django.urls import path, include
from . import views

urlpatterns = \
    [
        path('', views.users, name='users'),
        path('<int:user_id>/', views.user_item, name='user_item'),
        path('delete/<int:user_id>/', views.delete_user),
        path('signup/', views.register, name="create_user"),
        path('signup/<int:user_id>/', views.update_user, name="update_user"),
    ]
