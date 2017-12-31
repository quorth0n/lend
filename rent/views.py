from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.conf import settings

import firebase_admin
import os
from firebase_admin import auth, credentials

from .forms import LoginForm, ListingForm, ProfileForm 
from .models import Product, User

default_app = firebase_admin.initialize_app(credentials.Certificate(os.path.join(settings.BASE_DIR, 'rent/firebase.json')))

# Create your views here.
def index(req):
    #return HttpResponse("Welcome to /rent. This will be our index app.")
    return render(req, 'rent/index.html')

def auth(req):
    form = LoginForm()
    if req.method == "POST":
        form = LoginForm(req.POST)

        #We //CANNOT// check if this form is valid otherwise it doesn't process google & facebook
        token = firebase_admin.auth.verify_id_token(req.POST.get('auth_token', None))
        user = firebase_admin.auth.get_user(token['uid'])
        req.session['uid'] = user.uid
        req.session['email'] = user.email
        req.session['name'] = token.get('name')
        print(req.session['name']);

        #if form.is_valid():
            #print("Form is Valid")
            #token = firebase_admin.auth.verify_id_token(req.POST.get('auth_token', None))
            #user = firebase_admin.auth.get_user(token['uid'])
            #req.session['uid'] = user.uid
            #req.session['email'] = user.email
            #req.session['name'] = token.get('name')
        #print(vars(user))

    return render(req, 'rent/auth.html', {'form': form})

class ProductView(generic.DetailView):
    model = Product
    template_name = "rent/listing.html"

class UserView(generic.DetailView):
    model = User
    template_name = "rent/profile.html"

    def get_object(self):
        print(User.objects.get(uname=self.kwargs['uname']))
        return User.objects.get(uname=self.kwargs['uname'])

def plisting(req, product_id):
    #print(req.session['name']);
    return HttpResponse(req, "rent/listing.html")

def plisting_form(req):
    if 'name' not in req.session:
        return HttpResponseRedirect('/rent/auth')
    else:
        form = ListingForm()
        # if this is a POST req we need to process the form data
        if req.method == 'POST':
            # create a form instance and populate it with data from the req:
            form = ListingForm(req.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                print(form.cleaned_data)
                post_data = ListingForm(req.POST)
                new_product = post_data.save()
                new_product.owner = req.session['uid'] 
                new_product.save()

                # redirect to a new URL:
                return HttpResponseRedirect('/product/'+str(new_product.pk))

        return render(req, 'rent/plisting_form.html', {'form': form})

def profile_form(req, uname):
    print(req.session['name'])
    print(uname)
    if 'name' not in req.session or req.session['name'] != uname:
        return HttpResponseRedirect('/rent/auth')
    else:

        # if this is a POST req we need to process the form data
        if req.method == 'POST':
            # create a form instance and populate it with data from the req:
            if User.objects.filter(uname=uname).exists():
                user=User.objects.get(uname=uname)
                form = ProfileForm(req.POST, instance=user)
            else:
                form = ProfileForm(req.POST)

            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                print(form.cleaned_data)
                new_user = form.save()
                new_user.uname = req.session['name'] 
                new_user.save()
                #new_user.uname = req.session['name']
                #new_user.save()
                #form.save_m2m()
                #User.objects.get()req.session['uname']
                #post_data = ProfileForm(req.POST)
                #new_profile = post_data.save()
                #if not new_profile.uname:
                #    new_profile.uname = req.session['name']
                #new_profile.save()

                # redirect to a new URL:
                return HttpResponseRedirect('/user/'+str(new_user.uname))
        else:
            if User.objects.filter(uname=uname).exists():
                user=User.objects.get(uname=uname)
                form = ProfileForm(instance=user)
            else:
                form = ProfileForm()


        return render(req, 'rent/plisting_form.html', {'form': form})

