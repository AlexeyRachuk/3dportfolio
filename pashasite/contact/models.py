from django.db import models
from datetime import date

from solo.models import SingletonModel


class Contact(SingletonModel):
    title = models.CharField('Заголовок', max_length=60)
    descr = models.TextField('Описание')
    insta = models.CharField('Инстаграм', max_length=100, blank=True)

    def __str__(self):
        return "Контакты"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class FormContactPage(models.Model):
    name = models.CharField('Ваше имя', max_length=20)
    contact = models.CharField('Удобный способ связи', max_length=250)
    message = models.CharField('Сообщение', max_length=255)
    date = models.DateField('Дата публикации', default=date.today)

    class Meta:
        verbose_name = "Заявки с формы на странице Контакты"
        verbose_name_plural = "Заявки с формы на странице Контакты"

    def __str__(self):
        return "Заявки с формы на странице Контакты"
