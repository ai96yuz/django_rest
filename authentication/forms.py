from .models import CustomUser
from django import forms
from django.forms import TextInput


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'middle_name', 'last_name', 'email')
        widgets = {
            "first_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the First Name'}),
            "middle_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Middle Name'}),
            "last_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Last Name'}),
            "email": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the e-mail'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
