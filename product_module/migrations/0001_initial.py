# Generated by Django 4.2 on 2023-04-21 09:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import product_module.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام محصول')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='تصویر محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('quantity', models.IntegerField(default=1, verbose_name='موجودی')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='', max_length=200, null=True, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده / نشده')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ قرار گیری محصول')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='نام برند')),
                ('english_title', models.CharField(blank=True, db_index=True, default='', max_length=300, null=True, unique=True, verbose_name='نام در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='', null=True, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product_module.productcategory')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='ProductCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(db_index=True, max_length=10, validators=[product_module.validators.coupon_code_validator], verbose_name='کد کوپن')),
                ('discount_percent', models.CharField(blank=True, help_text='حتما از علامت (٪) در اخر استفاده کنید', max_length=4, null=True, validators=[product_module.validators.valid_pct], verbose_name='درصد تخفیف')),
                ('discount_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='مقدار قیمتی تخفیف')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('expires_date', models.DateTimeField(verbose_name='تاریخ انقضا')),
                ('discount_type', models.CharField(choices=[('Percent', 'درصدی'), ('Price', 'قیمتی')], max_length=8, verbose_name='نوع کوپن')),
            ],
            options={
                'verbose_name': 'کوپن تخفیف',
                'verbose_name_plural': 'کوپن های تخفیف',
            },
        ),
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
        migrations.CreateModel(
            name='TestDownload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(5, 'نمیتوانید بیشتر از 5 امتیاز برای محصول ثبت کنید'), django.core.validators.MinValueValidator(1, 'نمیتوانید کمتر از 1 امتیاز برای محصول ثبت کنید')], verbose_name='امتیاز')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='مربوط به محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر رای دهنده')),
            ],
            options={
                'verbose_name': 'امتیاز محصول',
                'verbose_name_plural': 'امتیازات محصول',
            },
        ),
        migrations.CreateModel(
            name='ProductVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='آی پی کاربر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_visit', to='product_module.product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'بازدید محصول',
                'verbose_name_plural': 'بازدیدهای محصول',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_gallery', to='product_module.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر گالری',
                'verbose_name_plural': 'گالری تصاویر',
            },
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
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commend_text', models.TextField(verbose_name='متن کامنت')),
                ('commend_mode', models.CharField(choices=[('Bad', 'بد'), ('Good', 'خوب'), ('Poker', 'پوکر')], max_length=50, verbose_name='مود کامنت')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('is_accepted', models.BooleanField(default=False, verbose_name='تایید شده توسط ادمین')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='برای محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brands', to='product_module.productbrand', verbose_name='برند'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_categories', to='product_module.productcategory', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
