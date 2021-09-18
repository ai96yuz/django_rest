from .models import Order
from django.forms import ModelForm, DateTimeInput, Select


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'book', 'plated_end_at', 'end_at')
        widgets = {
            "user": Select(attrs={'class': 'form-control', 'placeholder': 'Select User'}),
            "book": Select(attrs={'class': 'form-control', 'placeholder': 'Select Book'}),
            "plated_end_at": DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local', 'placeholder': 'book should be returned at'}),
            "end_at": DateTimeInput(format='%Y-%m-%dT%H:%M:%S', attrs={'type': 'datetime-local', 'placeholder': 'book is returned at'})
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields["user"].empty_label = "Select User"
        self.fields["book"].empty_label = "Select Book"
