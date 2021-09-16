from django.db import models
from django.shortcuts import render
from django.views import generic
from authentication.models import CustomUser
from .models import Order


def home(request):
    return render(request, "orders_home.html", {})


class AllOrdersCreated(generic.ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.all().order_by('-created_at') 
    template_name = 'all_orders_created_at.html'


class AllOrdersPlated(generic.ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.all().order_by('-plated_end_at') 
    template_name = 'orders_plated_at.html'

def book_by_user(request, user_id=111):
    template_name = 'book_detail_by_user.html'
    books = Order.objects.filter(user=user_id)
    user = CustomUser.objects.get(id=user_id)
    return render(request, template_name, {'books':books, "user":user})

class HandOverBook(generic.ListView):
    template_name = 'hand_over_book.html'
    context_object_name = 'orders'
    queryset = Order.objects.filter(end_at=None)

