# Generated by Django 4.1.5 on 2023-01-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_remove_productbrand_url_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbrand',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=300, null=True, verbose_name='نام در url'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True, verbose_name='عنوان در url'),
        ),
    ]
