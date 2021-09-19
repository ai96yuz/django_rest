from .models import Order
from django.forms import ModelForm, DateTimeInput, Select


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'plated_end_at')
        widgets = {
            "user": Select(attrs={'class': 'form-control', 'placeholder': 'Select User'}),
            "book": Select(attrs={'class': 'form-control', 'placeholder': 'Select Book'}),
            "plated_end_at": DateTimeInput(
                format='%Y-%m-%dT%H:%M:%S',
                attrs={'type': 'datetime-local', 'placeholder': 'book should be returned at'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["user"].empty_label = "Select User"
        self.fields["book"].empty_label = "Select Book"

# from .models import Order
# from django import forms
# from book.models import Book
# from authentication.models import CustomUser
#
#
# class OrderForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=CustomUser.objects.all(), empty_label='Choose the user', label='User', widget=forms.Select(attrs={'class': 'form-control'}))
#     book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label='Choose the book', label='Book', widget=forms.Select(attrs={'class': 'form-control'}))
#     plated_end_at = forms.DateTimeField(label='Plated at (YYYY-MM-DD HH:MM:SS)', widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}))

# from django.forms import ModelForm
# from .models import Order
#
#
# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = {'user', 'book', 'end_at', 'plated_end_at'}