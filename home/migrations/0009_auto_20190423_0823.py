# Generated by Django 2.2 on 2019-04-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190423_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_Img',
            field=models.ImageField(help_text='Enter field doc', upload_to=''),
        ),
    ]