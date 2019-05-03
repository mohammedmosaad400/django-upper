# Generated by Django 2.2 on 2019-04-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20190429_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_content',
            field=models.TextField(help_text='الإقتراح'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(blank=True, help_text='التاريخ', null=True),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_email',
            field=models.EmailField(help_text='البريد الإلكتروني', max_length=254),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_title',
            field=models.CharField(help_text='عنوان الإقتراح', max_length=500),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_writer',
            field=models.CharField(help_text='اسم المواطن', max_length=200),
        ),
    ]
