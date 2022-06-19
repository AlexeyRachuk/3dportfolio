from django.db import models

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
