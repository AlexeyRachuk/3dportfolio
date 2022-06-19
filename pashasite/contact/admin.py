from django import forms
from django.contrib import admin

from .models import Contact
from solo.admin import SingletonModelAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ContactAdminForm(forms.ModelForm):
    descr = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Contact
        fields = '__all__'


@admin.register(Contact)
class ContactAdmin(SingletonModelAdmin):
    fields = ('title', 'descr', 'insta')
    form = ContactAdminForm
