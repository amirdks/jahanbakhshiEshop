# Generated by Django 4.1.5 on 2023-01-14 15:17

from django.db import migrations, models
import product_module.validators


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0018_productcoupon_alter_productcomment_commend_mode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcoupon',
            options={'verbose_name': 'کوپن تخفیف', 'verbose_name_plural': 'کوپن های تخفیف'},
        ),
        migrations.AlterField(
            model_name='productcoupon',
            name='discount_percent',
            field=models.CharField(blank=True, help_text='حتما از علامت (٪) در اخر استفاده کنید', max_length=4, null=True, validators=[product_module.validators.valid_pct], verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='productcoupon',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='مقدار قیمتی تخفیف'),
        ),
        migrations.AlterField(
            model_name='productcoupon',
            name='discount_type',
            field=models.CharField(choices=[('Price', 'قیمتی'), ('Percent', 'درصدی')], max_length=8, verbose_name='نوع کوپن'),
        ),
    ]