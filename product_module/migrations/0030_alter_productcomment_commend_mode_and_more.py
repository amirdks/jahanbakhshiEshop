# Generated by Django 4.1.5 on 2023-04-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0029_productdetail_remove_product_battery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='commend_mode',
            field=models.CharField(choices=[('Good', 'خوب'), ('Bad', 'بد'), ('Poker', 'پوکر')], max_length=50, verbose_name='مود کامنت'),
        ),
        migrations.AlterField(
            model_name='productcoupon',
            name='discount_type',
            field=models.CharField(choices=[('Price', 'قیمتی'), ('Percent', 'درصدی')], max_length=8, verbose_name='نوع کوپن'),
        ),
    ]
