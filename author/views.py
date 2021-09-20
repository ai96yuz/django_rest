from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author
from rest_framework import viewsets
from .serializers import AuthorSerializer


def authors(request):
    return render(request, 'author/authors.html', {'authors': Author.objects.all()})


def author_item(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'name': author.name, 'surname': author.surname,
               'patronymic': author.patronymic,
               'id': author.id, 'books': author.books.all()}
    return render(request, 'author/author_details.html', context)


def create_author(request):
    if request.method != 'POST':
        new_author = AuthorForm()
        error = ''
    else:
        new_author = AuthorForm(request.POST)
        if new_author.is_valid():
            author_id = new_author.save().id
            return redirect('/author/', author_id)
        else:
            error = 'Form is incorrect!'

    context = {'author': new_author, 'error': error}
    return render(request, 'author/create_author.html', context)


def update_author(request, pk):
    if request.method != 'POST':
        updated_author = AuthorForm(instance=Author.get_by_id(pk))
        error = ''
    else:
        updated_author = AuthorForm(request.POST, instance=Author.get_by_id(pk))
        if updated_author.is_valid():
            author_id = updated_author.save().id
            return redirect('/author/', author_id)
        else:
            error = 'Form is incorrect'

    context = {'author': updated_author, 'error': error}
    return render(request, 'author/create_author.html', context)


def delete_author(request, pk):
    Author.delete_by_id(pk)
    return redirect('/author/')


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer