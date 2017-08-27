from django.shortcuts import render
from django.http import HttpResponse

import firebase_admin
from firebase_admin import credentials, auth

from .forms import LoginForm

default_app = firebase_admin.initialize_app(credentials.Certificate('firebase.json'))

# Create your views here.
def index(req):
    return HttpResponse("Welcome to /rent. This will be our index app.")

def auth(req):
    #form = LoginForm()
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            print("Form is Valid")
            auth = form.cleaned_data['auth_token']
            user = auth.get_user(uid)

    return render(req, 'rent/auth.html', {'form': form}) 
