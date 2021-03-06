# Generated by Django 3.0.8 on 2020-09-15 11:33

from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0003_products_categoris'),
    ]

    operations = [
        migrations.CreateModel(
            name='productsgallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_products.models.uplad_gallery_image_path, verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.products')),
            ],
        ),
    ]
