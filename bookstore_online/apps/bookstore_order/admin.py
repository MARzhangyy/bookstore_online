# coding=utf-8
from django.contrib import admin

from .models import OrderDetailInfo, OrderInfo


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):

    list_display = ["oid", "user", "ordertime", "ototal", "oaddress"]
    list_per_page = 5
    list_filter = ["user", "ordertime", "oaddress"]
    search_fields = ["user__uname"]
    ordering = ["-ordertime"]


@admin.register(OrderDetailInfo)
class OrderDetailInfoAdmin(admin.ModelAdmin):

    list_display = ["goods", "order", "price", "count"]
    list_per_page = 5
    list_filter = ["goods"]
