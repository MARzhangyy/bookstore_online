# coding=utf-8
from django.db import models
from tinymce.models import HTMLField  # 使用富文本编辑框要在settings文件中安装
# 将一对多的关系维护在GoodsInfo中维护，另外商品信息与分类信息都属于重要信息需要使用逻辑删除


class TypeInfo(models.Model):
    # 图书分类
    isDelete = models.BooleanField(default=False)
    ttitle = models.CharField(max_length=20, verbose_name="分类")

    class Meta:
        verbose_name = "商品类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    # 具体图书信息
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gtitle = models.CharField(max_length=50, verbose_name="图书名称", unique=True)
    gpicture = models.ImageField(upload_to='bookstore_goods', verbose_name="图片路径")
    gprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="商品价格")  # 商品价格小数位为两位，整数位为3位
    author = models.CharField(max_length=50,verbose_name='作者')
    press = models.CharField(max_length=50,verbose_name='出版社')
    publictime = models.CharField(max_length=20,verbose_name='出版时间')
    gclick = models.IntegerField(verbose_name="点击量")
    gintroduction = models.CharField(max_length=200, verbose_name="简介")
    gstock = models.IntegerField(verbose_name="库存")
    gdetails = HTMLField(max_length=10000, verbose_name="详情")
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE, verbose_name="分类")  # 外键关联TypeInfo表


    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gtitle
