# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_user', '0001_initial'),
        ('bookstore_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=6, decimal_places=2)),
                ('count', models.IntegerField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x95\xb0')),
                ('goods', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='bookstore_goods.GoodsInfo')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u8be6\u60c5',
                'verbose_name_plural': '\u8ba2\u5355\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(max_length=20, serialize=False, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7', primary_key=True)),
                ('ordertime', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x97\xb6\xe9\x97\xb4')),
                ('IsPay', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xaf\xe4\xbb\x98')),
                ('ototal', models.DecimalField(verbose_name=b'\xe6\x80\xbb\xe4\xbb\xb7', max_digits=8, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x9c\xb0\xe5\x9d\x80')),
                ('user', models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x94\xa8\xe6\x88\xb7', to='bookstore_user.UserInfo')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95', to='bookstore_order.OrderInfo'),
        ),
    ]
