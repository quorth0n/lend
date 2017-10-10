from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='plist')
    #url(r'^product/(?P<pk>[0-9]+)/$', views.plisting, name='plist')
]
