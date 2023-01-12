from django.contrib import admin

# Register your models here.
from site_module.models import SiteSetting, SiteEmailBanner


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteEmailBanner)
class SiteEmailBannerAdmin(admin.ModelAdmin):
    pass
