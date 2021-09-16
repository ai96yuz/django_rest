from django.shortcuts import render
from django.views import generic

from author.models import Author
from book.models import Book


class AuthorListView(generic.ListView):
    model = Author

    context_object_name = 'authors'
    queryset = Author.objects.all()
    template_name = 'all_authors.html'


def author_detail_view(request, author_id):
    template_name = "author_details.html"
    author = Author.get_by_id(author_id)
    books = list(Book.objects.filter(authors__id=author_id))

    return render(request, template_name, {"books": books, "author": author})
