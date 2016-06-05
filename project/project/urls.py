from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^CRUD/', include('CRUD.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
