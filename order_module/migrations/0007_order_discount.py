# Generated by Django 4.1.5 on 2023-01-14 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0018_productcoupon_alter_productcomment_commend_mode'),
        ('order_module', '0006_alter_orderdetail_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productcoupon', verbose_name='تخفیف'),
        ),
    ]
