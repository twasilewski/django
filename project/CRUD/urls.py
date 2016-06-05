from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from CRUD.models import Item
from CRUD import views
#from . import views

urlpatterns = [ url(r'^$', views.index, name='CRUD'),
                url(r'^item/(?P<item_id>\d+)$', views.item, name = 'item'),
                url(r'^update/(?P<item_id>\d+)$', views.update, name = 'item'),
                #url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Item, template_name="CRUD/item.html")),
                url(r'^add_item/$', views.add_item, name='add_item'),
                url(r'^delete/(?P<item_id>\d+)$', views.delete, name = 'item')
              ]

#urlpatterns = [url(r'^$', views.index, name='CRUD')]
