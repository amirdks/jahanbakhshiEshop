from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True, verbose_name='ایمیل')
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()

        return self.email

    def set_password(self, raw_password):
        if len(raw_password) < 8:
            return ValidationError('رمز عبور نمیتواند کمتر از 8 کارکتر باشد')
        else:
            super(User, self).set_password(raw_password)
