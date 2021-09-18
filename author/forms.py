from django.forms import ModelForm, TextInput
from .models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic']
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the First Name'}),
            "surname": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Surname'}),
            "patronymic": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Patronymic'}),
        }
