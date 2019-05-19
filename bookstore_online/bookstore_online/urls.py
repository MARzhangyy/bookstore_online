#coding=utf-8
"""bookstore_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bookstore_goods.urls', namespace='bookstore_goods')),
    url(r'^user/', include('bookstore_user.urls', namespace='bookstore_user')),
    url(r'^cart/', include('bookstore_cart.urls', namespace='bookstore_cart')),
    url(r'^order/', include('bookstore_order.urls', namespace='bookstore_order')),
    url(r'^tinymce/', include('tinymce.urls')),  # 使用富文本编辑框配置conf
]
