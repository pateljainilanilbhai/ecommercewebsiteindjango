from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Address
from django.forms import ModelForm
from django_countries.fields import CountryField
from django_countries.data import COUNTRIES

class useraddaddressform(ModelForm):
    class Meta:
        model = Address
        fields = ['full_name','phone_number','country','postcode','town_or_city','street_address_1','street_address_2','county']




class UserLoginForm(forms.Form):
    """
    Used by the user to enter login credentials
    """
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class UserRegistrationForm(UserCreationForm):
    """
    Used by the user to sign up with the website
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


