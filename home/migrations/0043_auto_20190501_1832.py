# Generated by Django 2.2 on 2019-05-01 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20190501_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Complaint_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 1, 18, 32, 31, 435943), help_text='التاريخ', null=True, verbose_name='الوقت والتاريخ'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 1, 18, 32, 31, 436944), help_text='التاريخ', null=True, verbose_name='الوقت والتاريخ'),
        ),
    ]