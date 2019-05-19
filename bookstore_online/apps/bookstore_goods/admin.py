# coding=utf-8
from django.contrib import admin
from .models import TypeInfo, GoodsInfo


# 注册模型类
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']
    list_per_page = 10
    search_fields = ['ttitle']
    list_display_links = ['ttitle']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'gtitle', 'gpicture', 'gprice',
                    'author','press','publictime','gclick', 'gstock',
                    'gintroduction','gdetails']
    list_editable = ['gstock', 'gdetails', 'gintroduction']
    readonly_fields = ['gclick']
    search_fields = ['gtitle', 'gdetails', 'gintroduction']
    list_display_links = ['gtitle']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
