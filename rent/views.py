from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

import firebase_admin
from firebase_admin import auth, credentials

from .forms import LoginForm
from .models import Product

default_app = firebase_admin.initialize_app(credentials.Certificate('firebase.json'))

# Create your views here.
def index(req):
    print(req.session['email'])
    return HttpResponse("Welcome to /rent. This will be our index app.")

def auth(req):
    form = LoginForm()
    if req.method == "POST":
        form = LoginForm(req.POST)

        if form.is_valid():
            print("Form is Valid")
            token = firebase_admin.auth.verify_id_token(req.POST.get('auth_token', None))
            user = firebase_admin.auth.get_user(token['uid'])
            req.session['uid'] = user.uid
            req.session['email'] = user.email
            req.session['name'] = token.get('name')
        #print(vars(user)) 

    return render(req, 'rent/auth.html', {'form': form})

class ProductView(generic.DetailView):
    model = Product
    template_name = "rent/listing.html"


#def plisting(req, product_id):
    #return HttpResponse("/product/")
