from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='plist'),
    url(r'^user/(?P<uname>[a-zA-Z0-9_-]+)/$', views.UserView.as_view(), name='user'),
    url(r'^new/$', views.plisting_form, name='plist_f'),
    url(r'^user/(?P<uname>[a-zA-Z0-9_-]+)/edit/$', views.profile_form, name='user_f'),
    #url(r'^product/(?P<pk>[0-9]+)/$', views.plisting, name='plist')
]
