# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gdetails',
            field=tinymce.models.HTMLField(max_length=10000, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'\xe5\x9b\xbe\xe4\xb9\xa6\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
