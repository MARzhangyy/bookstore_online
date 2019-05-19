# coding=utf-8
from django.conf.urls import url

from . import views

app_name = 'bookstore_order'

urlpatterns = [
    url(r'^$', views.order, name="order"),
    url(r'^push/$', views.order_handle, name="push"),
]