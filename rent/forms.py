from django import forms
from .models import Product, User

class LoginForm(forms.Form):
    email = forms.EmailField(label='')
    password = forms.CharField(widget=forms.PasswordInput(), label='')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'age', 'method', 'price', 'lat', 'lng']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['bio', 'lat', 'lng']
