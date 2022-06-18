from django.contrib import admin
from django.contrib.admin import TabularInline
from solo.admin import SingletonModelAdmin

from .models import ImageSet, Works, Home


class ImageInline(admin.TabularInline):
    model = ImageSet
    extra = 1


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
class HomeAdmin(SingletonModelAdmin):
    fields = ('title', 'description', 'copywrite', 'insta', 'telega', 'vk')
