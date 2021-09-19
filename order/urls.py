from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.orders, name='orders'),
        path('delete/<int:order_id>/', views.delete_order),
        path('create/', views.create_order, name='create_order'),
        path('update/<int:order_id>/', views.create_order, name='update_orders'),
    ]
