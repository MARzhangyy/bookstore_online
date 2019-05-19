# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('gtitle', models.CharField(unique=True, max_length=20, verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe5\x90\x8d\xe7\xa7\xb0')),
                ('gpicture', models.ImageField(upload_to=b'bookstore_goods', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe8\xb7\xaf\xe5\xbe\x84')),
                ('gprice', models.DecimalField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe4\xbb\xb7\xe6\xa0\xbc', max_digits=5, decimal_places=2)),
                ('author', models.CharField(max_length=50, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('press', models.CharField(max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe7\xa4\xbe')),
                ('publictime', models.CharField(max_length=20, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe6\x97\xb6\xe9\x97\xb4')),
                ('gclick', models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f')),
                ('gintroduction', models.CharField(max_length=200, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('gstock', models.IntegerField(verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('gdetails', tinymce.models.HTMLField(max_length=200, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isDelete', models.BooleanField(default=False)),
                ('ttitle', models.CharField(max_length=20, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u7c7b\u578b',
                'verbose_name_plural': '\u5546\u54c1\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='bookstore_goods.TypeInfo'),
        ),
    ]
