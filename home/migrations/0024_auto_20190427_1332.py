# Generated by Django 2.2 on 2019-04-27 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20190427_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news2',
            options={'ordering': ['news_Title', 'news_Img', 'news_Content']},
        ),
        migrations.RenameField(
            model_name='news2',
            old_name='news2_Content',
            new_name='news_Content',
        ),
        migrations.RenameField(
            model_name='news2',
            old_name='news2_Date',
            new_name='news_Date',
        ),
        migrations.RenameField(
            model_name='news2',
            old_name='news2_Img',
            new_name='news_Img',
        ),
        migrations.RenameField(
            model_name='news2',
            old_name='news2_Title',
            new_name='news_Title',
        ),
    ]