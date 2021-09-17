from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm, TextInput, NumberInput, Select, SelectMultiple
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'name of book'}),
            "description": TextInput(attrs={'class': 'form-control', 'placeholder': 'book description'}),
            "count": NumberInput(attrs={'class': 'form-control', 'placeholder': 'book count'}),
            "authors": SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'authors'})
        }

    def book_check(self):
        if self.data['name'] is None:
            return False
        try:
            Book.objects.get(name=self.data['name'])
            return False
        except ObjectDoesNotExist:
            pass

        return True
