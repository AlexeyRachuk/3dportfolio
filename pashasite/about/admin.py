from django import forms
from django.contrib import admin

from .models import About
from solo.admin import SingletonModelAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AboutAdminForm(forms.ModelForm):
    desr = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = '__all__'


@admin.register(About)
class AboutAdmin(SingletonModelAdmin):
    fields = ('title', 'desr', 'image')
    form = AboutAdminForm
