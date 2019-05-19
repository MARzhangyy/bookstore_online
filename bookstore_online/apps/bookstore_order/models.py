# coding=utf-8
from django.db import models

from bookstore_goods.models import GoodsInfo
from bookstore_user.models import UserInfo

class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True, verbose_name="订单号")
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="订单用户")
    ordertime = models.DateTimeField(auto_now=True, verbose_name="时间")
    IsPay = models.BooleanField(default=False, verbose_name="是否支付")
    ototal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="总价")
    oaddress = models.CharField(max_length=150, verbose_name="订单地址")

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}在的订单{1}".format(self.user.uname, self.ordertime)


# 无法实现：真实支付，物流信息
class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品")  # 关联商品信息
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name="订单")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="商品价格")
    count = models.IntegerField(verbose_name="商品数")

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}(数量为{1})".format(self.goods.gtitle, self.count)