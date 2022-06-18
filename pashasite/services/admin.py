from django.contrib import admin
from django.contrib.admin import TabularInline
from solo.admin import SingletonModelAdmin

from .models import ServicesMain, ServicesBig, ServicesSmall, ServicesIcon


class ServicesBigAdmin(admin.TabularInline):
    model = ServicesBig
    extra = 1


class ServicesSmallAdmin(admin.TabularInline):
    model = ServicesSmall
    extra = 1


@admin.register(ServicesIcon)
class ServicesIconAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_code']


@admin.register(ServicesMain)
class ServicesMainAdmin(SingletonModelAdmin):
    fields = ('title', 'descr', 'title_more')
    inlines = [
        ServicesBigAdmin,
        ServicesSmallAdmin,
    ]
