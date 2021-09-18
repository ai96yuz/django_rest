from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import Order


def orders(request):
    return render(request, 'order/orders.html', {'orders': Order.objects.all()})


def order_item(request, order_id):
    order = Order.objects.get(pk=order_id)
    context = {'user': order.user, 'book': order.book, 'created_at': order.created_at,
               'end_at': order.end_at, 'plated_end_at': order.plated_end_at
               }

    return render(request, 'order/order_details.html', context)


def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    return redirect('orders')


def orders_form(request, order_id=0):
    if request.method == "GET":
        if order_id == 0:
            form = OrderForm()
        else:
            order = Order.objects.get(pk=order_id)
            form = OrderForm(instance=order)
        return render(request, "order/orders_form.html", {"form": form})
    else:
        if order_id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(pk=order_id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect("orders")
