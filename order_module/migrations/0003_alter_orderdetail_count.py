# Generated by Django 4.1.5 on 2023-01-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0002_alter_orderdetail_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='count',
            field=models.PositiveIntegerField(verbose_name='تعداد'),
        ),
    ]
