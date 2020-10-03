# Generated by Django 3.0.8 on 2020-09-16 08:05

from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_productsgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsgallery',
            options={'verbose_name': 'تصویر', 'verbose_name_plural': 'تصاویر'},
        ),
        migrations.AlterField(
            model_name='productsgallery',
            name='image',
            field=models.ImageField(upload_to=eshop_products.models.uplad_gallery_image_path, verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='productsgallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.products', verbose_name='محصول'),
        ),
    ]