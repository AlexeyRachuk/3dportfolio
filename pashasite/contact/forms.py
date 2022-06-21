from django import forms
from django.forms import TextInput, Textarea

from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = FormContactPage
        fields = ['name', 'contact', 'message']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя',
            }),
            "contact": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Удобный способ связи',
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'cols': '30',
                'rows': '10',
                'placeholder': 'Сообщение',
            })

        }
