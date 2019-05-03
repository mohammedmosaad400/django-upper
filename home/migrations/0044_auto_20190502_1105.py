# Generated by Django 2.2 on 2019-05-02 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20190501_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Complaint_replay',
            field=models.TextField(default='لم يتم الرد بعد ...', verbose_name='الرد على الشكوى'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Complaint_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 2, 11, 5, 52, 670775), help_text='التاريخ', null=True, verbose_name='الوقت والتاريخ'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 2, 11, 5, 52, 670775), help_text='التاريخ', null=True, verbose_name='الوقت والتاريخ'),
        ),
    ]