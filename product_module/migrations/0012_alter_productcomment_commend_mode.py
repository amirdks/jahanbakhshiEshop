# Generated by Django 4.1.5 on 2023-01-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0011_alter_productcomment_commend_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='commend_mode',
            field=models.CharField(choices=[('Bad', 'بد'), ('Good', 'خوب'), ('Poker', 'پوکر')], max_length=50, verbose_name='مود کامنت'),
        ),
    ]
