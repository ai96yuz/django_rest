from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Book
from order.models import Order
from .forms import BookForm


def books(request):
    if request.method == 'GET':
        return render(request, 'book/books.html', {'books': Book.get_all()})
    if request.method == 'POST':
        get_select_value = request.POST.get('filter_menu')
        get_input_value = request.POST.get('title')
        if get_select_value == 'Show specific book (enter id)':
            return render(request, 'book/books.html', {'books': [Book.get_by_id(int(get_input_value))]})
        elif get_select_value == 'Show all books by name of author':
            return render(request, 'book/books.html', {'books': show_books_by_name_author(get_input_value)})
        elif get_select_value == 'Show all books sorted by name asc':
            return render(request, 'book/books.html', {'books': Book.objects.all().order_by('name')})
        elif get_select_value == 'Show all books sorted by name desc':
            return render(request, 'book/books.html', {'books': Book.objects.all().order_by('-name')})
        elif get_select_value == 'Show all books sorted by count':
            return render(request, 'book/books.html', {'books': Book.objects.all().order_by('count')})
        elif get_select_value == 'Show all unordered book':
            return render(request, 'book/books.html', {'books': get_unordered_books()})
        else:
            return render(request, 'book/books.html', {'books': Book.get_all()})


def show_books_by_name_author(get_input_value):
    res = []
    for elem in Book.get_all():
        for br in elem.authors.all():
            if br.name == get_input_value or br.surname == get_input_value or br.patronymic == get_input_value:
                res.append(elem)
    return res


def get_unordered_books():
    all_books = Book.get_all()
    all_orders = Order.get_all()
    get_all_ordered_books = []
    for book in all_books:
        for order in all_orders:
            if book.id == order.book.id:
                get_all_ordered_books.append(book)
    get_all_unordered_books = set(all_books) - set(get_all_ordered_books)
    return get_all_unordered_books


def book_item(request, book_id):
    book = Book.objects.get(pk=book_id)
    amount_left = book.count - Order.objects.filter(book=book_id, end_at=None).count()
    context = {'title': book.name, 'id': book.id, 'authors': book.get_authors,
               'count': book.count, 'amount_left': amount_left, 'description': book.description}

    return render(request, 'book/book_details.html', context)


def create_book(request):
    if request.method != 'POST':
        new_book = BookForm()
        error = ''
    else:
        new_book = BookForm(request.POST)
        if new_book.is_valid() and new_book.book_check():
            book_id = new_book.save().id
            return redirect('/book/', book_id)
        else:
            error = 'Form is incorrect!'

    context = {'book': new_book, 'error': error}
    return render(request, 'book/create_book.html', context)


def update_book(request, pk):
    if request.method != 'POST':
        updated_book = BookForm(instance=Book.get_by_id(pk))
        error = ''
    else:
        updated_book = BookForm(request.POST, instance=Book.get_by_id(pk))
        if updated_book.is_valid() and updated_book.book_check():
            book_id = updated_book.save().id
            return redirect('/book/', book_id)
        else:
            error = 'Form is incorrect'

    context = {'book': updated_book, 'error': error}
    return render(request, 'book/create_book.html', context)


def delete_book(request, pk):
    Book.delete_by_id(pk)
    return redirect('/book/')


def book_search(request):
    search_box = request.GET['search_box']
    list_books = list(Book.objects.filter(Q(description__contains=search_box) | Q(name__contains=search_box)))

    return render(request, 'book/book_search.html', {"list_books": list_books, "page_title": 'We found this books for you!!'})

