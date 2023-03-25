# Generated by Django 4.1.5 on 2023-03-25 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0026_alter_productcoupon_discount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='commend_mode',
            field=models.CharField(choices=[('Good', 'خوب'), ('Poker', 'پوکر'), ('Bad', 'بد')], max_length=50, verbose_name='مود کامنت'),
        ),
        migrations.AlterField(
            model_name='productcoupon',
            name='discount_type',
            field=models.CharField(choices=[('Percent', 'درصدی'), ('Price', 'قیمتی')], max_length=8, verbose_name='نوع کوپن'),
        ),
    ]