from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import ImageSet, Works, Home


class ImageInline(TabularInline):
    model = ImageSet


@admin.register(Works)
class WorksAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'draft']
    inlines = [
        ImageInline,
    ]
    list_editable = ('draft',)
    prepopulated_fields = {'url': ('title',)}

    class Meta:
        model = Works


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
