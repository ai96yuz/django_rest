from django.contrib.auth import authenticate

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




class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'middle_name', 'email', 'password']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(username=email, password=password):
                raise forms.ValidationError("Invalid login")
