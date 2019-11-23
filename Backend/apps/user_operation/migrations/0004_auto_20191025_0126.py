# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-25 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0003_auto_20191011_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, help_text='When the item is added in wish list', verbose_name='Add Time'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='goods',
            field=models.ForeignKey(help_text='Product Id', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='Goods'),
        ),
    ]