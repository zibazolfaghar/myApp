# Generated by Django 3.0.8 on 2020-09-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.SlugField(max_length=120, verbose_name='عنوان در url'),
        ),
    ]