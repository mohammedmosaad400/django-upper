# Generated by Django 2.2 on 2019-04-30 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20190430_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization_Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('law_title', models.CharField(help_text='الوثيقة', max_length=1000)),
                ('law_date', models.DateField(help_text='التاريخ')),
                ('law_content', models.FileField(help_text='ملف الوثيقة', upload_to='')),
            ],
            options={
                'ordering': ['law_title', 'law_date', 'law_content'],
            },
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 30, 14, 47, 8, 106483), help_text='التاريخ', null=True),
        ),
    ]
