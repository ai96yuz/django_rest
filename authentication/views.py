from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserRegistrationForm
from order.models import Order
from rest_framework import generics
from .serializers import *


def users(request):
    return render(request, 'authentication/users.html', {'users': CustomUser.objects.all()})


def user_item(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    context = {'first_name': user.first_name, 'middle_name': user.middle_name, 'last_name': user.last_name,
               'id': user.id, 'email': user.email, 'role': user.role, 'is_active': user.is_active,
               'orders': Order.objects.filter(user=user_id)}

    return render(request, 'authentication/user_details.html', context)


def user_profile(request):
    return redirect('users')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'authentication/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'user_form': user_form})


def update_user(request, user_id):
    if request.method == "GET":
        if user_id == 0:
            form = UserRegistrationForm()
        else:
            user = CustomUser.objects.get(pk=user_id)
            form = UserRegistrationForm(instance=user)
        return render(request, "authentication/update_user.html", {"user_form": form})
    else:
        if user_id == 0:
            form = UserRegistrationForm(request.POST)
        else:
            user = CustomUser.objects.get(pk=user_id)
            form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid:
            form.save()
            return redirect(f"/users/{user_id}/")


def delete_user(request, user_id):
    CustomUser.delete_by_id(user_id)
    return redirect('users')


class UserListCreate(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = CustomUserCommonSerializer
    queryset = CustomUser.objects.all()


class UserViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserCommonSerializer
    queryset = CustomUser.objects.all()


class OrdersListForUser(generics.ListAPIView):
    serializer_class = CustomUserOrdersSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=kwargs['user_pk'])
        return self.list(request, *args, **kwargs)
