"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

from book import urls as book_urls
from author import urls as author_urls
from authentication import urls as user_urls
from order import urls as order_urls

urlpatterns = [
    path('', base_view, name="home"),
    path('admin/', admin.site.urls),
    path('books/', include(book_urls)),
    path('authors/', include(author_urls)),
    path('orders/', include(order_urls)),
    path('users/', include(user_urls)),
]