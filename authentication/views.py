from django.shortcuts import render
from django.views import generic
from book.models import Book

from .models import CustomUser


class UserListView(generic.ListView):
    model = CustomUser

    context_object_name = 'users'
    queryset = CustomUser.objects.all()
    template_name = 'all_users.html'


def user_detail_view(request, user_id):
    template_name = "user_details.html"
    user = CustomUser.get_by_id(user_id)

    return render(request, template_name, {"user": user, "page_title": user.first_name})
