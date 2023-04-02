# Generated by Django 4.1.5 on 2023-03-26 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0028_productcategory_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255, verbose_name='مقدار کلید')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.productcategory', verbose_name='دسته بندی مربوطه')),
            ],
            options={
                'verbose_name': 'جزییات محصول',
                'verbose_name_plural': 'جزییات محصولات',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='camera_resolution',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='product',
            name='gpu',
        ),
        migrations.RemoveField(
            model_name='product',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='screen_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='software',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='commend_mode',
            field=models.CharField(choices=[('Poker', 'پوکر'), ('Bad', 'بد'), ('Good', 'خوب')], max_length=50, verbose_name='مود کامنت'),
        ),
        migrations.CreateModel(
            name='ProductDetailValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(db_index=True, max_length=255, verbose_name='مقدار')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_attributes', to='product_module.product', verbose_name='محصول مربوطه')),
                ('product_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_detail_attributes', to='product_module.productdetail', verbose_name='جزییات مربوطه')),
            ],
            options={
                'verbose_name': 'مقدار جزییات محصول',
                'verbose_name_plural': 'مقدار جزییات محصولات',
                'ordering': ['product_detail__key'],
            },
        ),
    ]
