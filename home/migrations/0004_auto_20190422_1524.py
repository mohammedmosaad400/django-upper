# Generated by Django 2.2 on 2019-04-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190422_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_Date',
            field=models.DateTimeField(blank=True, help_text='Enter the date', null=True),
        ),
    ]
