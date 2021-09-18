from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.orders, name='orders'),
        path('delete/<int:order_id>/', views.delete_order),
        path('form', views.orders_form, name='create_orders'),
        path('form/<int:order_id>/', views.orders_form, name='update_orders'),
    ]
