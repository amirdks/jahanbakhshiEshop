# Generated by Django 4.1.5 on 2023-01-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_productbrand_slug_alter_productcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ قرار گیری محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, null=True, unique=True, verbose_name='عنوان در url'),
        ),
    ]
