# Generated by Django 2.2 on 2019-04-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_suggestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='News2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news2_Title', models.CharField(help_text='Enter news title', max_length=200)),
                ('news2_Img', models.ImageField(help_text='Upload Image', upload_to='home/static/img')),
                ('news2_Date', models.DateTimeField(blank=True, help_text='Enter the date', null=True)),
                ('news2_Content', models.TextField(help_text='Enter news content')),
            ],
            options={
                'ordering': ['news2_Title', 'news2_Img', 'news2_Content'],
            },
        ),
        migrations.AlterModelOptions(
            name='suggestion',
            options={'ordering': ['suggestion_title', 'suggestion_writer', 'suggestion_email', 'suggestion_date', 'suggestion_content']},
        ),
    ]
