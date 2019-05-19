# coding=utf-8
from django.contrib import admin

from .models import UserInfo, BooksBrowser


class UserInfoAdmin(admin.ModelAdmin):
    #设置列表可显示的字段
    list_display = ["uname", "uemail", "urecieve", "uaddress", "zipcode", "ucontact"]
    #每页显示条目数
    list_per_page = 5
    #设置过滤选项
    list_filter = ["uname", "zipcode"]
    #搜索字段
    search_fields = ["uname", "zipcode"]
    #设置列表中为只读字段，不能修改
    readonly_fields = ["uname"]


class BooksBrowserAdmin(admin.ModelAdmin):
    list_display = ["user", "good"]
    list_per_page = 50
    list_filter = ["user__uname", "good__gtitle"]
    search_fields = ["user__uname", "good__gtitle"]
    readonly_fields = ["user", "good"]
    #列表定时刷新
    refresh_times = [3, 5]


admin.site.site_header = '在线书店后台管理系统'
admin.site.site_title = '在线书店后台管理系统'

#自定义数据表显示字段
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(BooksBrowser, BooksBrowserAdmin)