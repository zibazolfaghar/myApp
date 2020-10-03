# Generated by Django 3.0.8 on 2020-09-15 07:22

from django.db import migrations, models
import eshop_slider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('link', models.URLField(verbose_name='آدرس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_slider.models.uplad_image_path, verbose_name='تصویر')),
            ],
        ),
    ]