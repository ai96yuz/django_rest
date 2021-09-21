from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/order', views.OrderView)

urlpatterns = \
    [
        path('all_orders/', views.orders, name='orders'),
        path('delete/<int:order_id>/', views.delete_order),
        path('create/', views.create_order, name='create_order'),
        path('update/<int:order_id>/', views.create_order, name='update_orders'),
        path('', include(router.urls))
    ]
