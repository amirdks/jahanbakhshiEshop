from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    telegram_number = models.CharField(max_length=200, null=True, blank=True, verbose_name='شماره تلگرام')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(unique=True, verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class SiteEmailBanner(models.Model):
    alt_text = models.CharField(max_length=30, verbose_name='متن جایگزین')
    banner = models.ImageField(upload_to='images/site-banner/', verbose_name='عکس بنر')
    is_active_banner = models.BooleanField(unique=True, verbose_name='بنر فعال')

    class Meta:
        verbose_name = 'بنر سایت'
        verbose_name_plural = 'بنر'

    def __str__(self):
        return self.alt_text
