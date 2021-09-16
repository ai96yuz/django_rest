from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from book.models import Book


# class BookListView(generic.ListView):
#     model = Book
#
#     context_object_name = 'books'
#     queryset = Book.objects.all()
#     template_name = 'all_books.html'


class UnorderedBookListView(generic.ListView):
    model = Book

    context_object_name = 'books'
    queryset = Book.objects.all()
    template_name = 'book_unordered.html'


def book_detail_view(request, book_id):
    template_name = "book_details.html"
    book = Book.get_by_id(book_id)

    return render(request, template_name, {"book": book, "page_title": book.name})


def all_books_view(request):
    template_name = "all_books.html"
    context = {}
    books = Book.get_all()
    paginator = Paginator(books, 6)
    page = request.GET.get('page', 1)
    try:
        context["books"] = paginator.page(page)
    except PageNotAnInteger:
        context["books"] = paginator.page(1)
    except EmptyPage:
        context["books"] = paginator.page(paginator.num_pages)

    context["page_title"] = "Books in stock"
    context["page"] = page

    return render(request, template_name, context)


def book_search(request):
    search = request.GET['search_box']

    list_books = list(Book.objects.filter(Q(description__contains=search) | Q(name__contains=search)))
    return render(request, 'books.html', {"list_books": list_books, "page_title": 'We found this books for you!!'})

def sort_book_asc(request):
    template_name = "sort_book_by_asc.html"
    books = Book.objects.all().order_by('name')

    return render(request, template_name, {'books':books})

def sort_book_desc(request):
    template_name = "sort_book_by_desc.html"
    books = Book.objects.all().order_by('-name')

    return render(request, template_name, {'books':books})

def sort_book_count(request):
    template_name = "sort_book_by_count.html"
    books = Book.objects.all().order_by('-count')

    return render(request, template_name, {'books':books})
