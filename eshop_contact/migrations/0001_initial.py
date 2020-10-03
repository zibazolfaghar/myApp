# Generated by Django 3.0.8 on 2020-09-17 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')),
                ('Email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name='عنوان پیام')),
                ('text', models.TextField(verbose_name='متن پیام')),
                ('is_read', models.BooleanField(verbose_name='خوانده شده/ نشده')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدرها',
            },
        ),
    ]