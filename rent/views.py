from django.shortcuts import render
from django.http import HttpResponse

import firebase_admin
from firebase_admin import credentials

from .forms import LoginForm

# Create your views here.
def index(req):
    return HttpResponse("Welcome to /rent. This will be our index app.")

def auth(req):
    default_app = firebase_admin.initialize_app(credentials.Certificate('firebase.json'))
    form = LoginForm()
    return render(req, 'rent/auth.html', {'form': form}) 
