from django.shortcuts import render, redirect
import datetime

from rest_framework import viewsets

from .forms import OrderForm
from .models import Order
from .serializers import OrderSerializer


def orders(request):
    get_all_orders = Order.objects.all()
    if request.method == 'GET':
        return render(request, 'order/orders.html', {'orders': get_all_orders})
    if request.method == 'POST':
        get_select_value = request.POST.get('filter_menu')
        get_input_value = request.POST.get('title')
        if get_select_value == 'Show all users who does not hand over books on time':
            return render(request, 'order/orders.html', {'orders': debtor_users()})
        elif get_select_value == 'Show all books ordered by specific user (enter user id)':
            return render(request, 'order/orders.html', {'orders': show_orders_of_specific_user(int(get_input_value))})
        elif get_select_value == 'Show all orders sorted by created date':
            return render(request, 'order/orders.html', {'orders': Order.objects.all().order_by('created_at')})
        elif get_select_value == 'Show all orders sorted by planed date':
            return render(request, 'order/orders.html', {'orders': Order.objects.all().order_by('plated_end_at')})
        else:
            return render(request, 'order/orders.html', {'orders': get_all_orders})


def show_orders_of_specific_user(get_input_value):
    result = []
    for elem in Order.get_all():
        if elem.user.id == get_input_value:
            result.append(elem)
    return result


def debtor_users():
    now = datetime.datetime.now().timestamp()
    result = []
    for elem in Order.get_all():
        if elem.end_at:
            if elem.end_date.timestamp() > elem.plated_end_at.timestamp():
                result.append(elem)
        else:
            if elem.plated_end_at.timestamp() < now:
                result.append(elem)
    return result


def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    return redirect('orders')


def create_order(request, order_id=0):
    if request.method == "GET":
        if order_id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=order_id)
            form = OrderForm(instance=order)
        return render(request, "order/create_order.html", {"form": form})
    else:
        if order_id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=order_id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect("orders")

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer