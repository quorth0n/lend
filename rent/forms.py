from django import forms
from .models import Product

class LoginForm(forms.Form):
    email = forms.EmailField(label='')
    password = forms.CharField(widget=forms.PasswordInput(), label='')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'age', 'method', 'price', 'lat', 'lng']

