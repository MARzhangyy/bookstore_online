# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksBrowser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('browser_time', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x97\xb6\xe9\x97\xb4')),
                ('good', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81ID', to='bookstore_goods.GoodsInfo')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u6d4f\u89c8\u8bb0\u5f55',
                'verbose_name_plural': '\u7528\u6237\u6d4f\u89c8\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(unique=True, max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('upwd', models.CharField(max_length=40, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81')),
                ('uemail', models.EmailField(unique=True, max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('urecieve', models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('uaddress', models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('zipcode', models.CharField(default=b'', max_length=6, verbose_name=b'\xe9\x82\xae\xe7\xbc\x96')),
                ('ucontact', models.CharField(default=b'', max_length=11, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe6\x96\xb9\xe5\xbc\x8f')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u57fa\u672c\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u57fa\u672c\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='booksbrowser',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', to='bookstore_user.UserInfo'),
        ),
    ]
