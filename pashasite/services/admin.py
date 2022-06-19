from django import forms
from django.contrib import admin
from django.contrib.admin import TabularInline
from solo.admin import SingletonModelAdmin

from .models import ServicesMain, ServicesBig, ServicesSmall, ServicesIcon


from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ServicesMainAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Описание страницы', widget=CKEditorUploadingWidget())

    class Meta:
        model = ServicesMain
        fields = '__all__'


class ServicesBigAdmin(admin.TabularInline):
    model = ServicesBig
    extra = 1
    form = ServicesMainAdminForm


class ServicesSmallAdmin(admin.TabularInline):
    model = ServicesSmall
    extra = 1
    form = ServicesMainAdminForm


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
    form = ServicesMainAdminForm
