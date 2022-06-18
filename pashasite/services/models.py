from django.db import models
from solo.models import SingletonModel


class ServicesMain(SingletonModel):
    title = models.CharField('Заголовок страницы', max_length=60)
    descr = models.TextField('Описание страницы')
    title_more = models.CharField('Дополнительно', max_length=60)

    def __str__(self):
        return "Страница услуг"

    class Meta:
        verbose_name = 'Страница услуг'
        verbose_name_plural = 'Страница услуг'


class ServicesIcon(models.Model):
    title = models.CharField('Название иконки', max_length=100)
    icon_code = models.CharField('Код иконки', max_length=100)

    def __str__(self):
        return self.icon_code

    class Meta:
        verbose_name = 'Иконки услуг'
        verbose_name_plural = 'Иконки услуг'


class ServicesBig(models.Model):
    order = models.SmallIntegerField('Сортировка', default=0)
    works = models.ForeignKey(ServicesMain, verbose_name='Большая услуга', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='big_service')
    title = models.CharField('Заголовок услуги', max_length=100)
    descr = models.TextField('Описание Услуги')
    icon = models.ForeignKey(ServicesIcon, verbose_name='Иконка услуги', null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='icon_big_service')
    draft = models.BooleanField("Публикация", default=True)

    def __str__(self):
        return "Большие услуги"

    class Meta:
        verbose_name = 'Большие услуги'
        verbose_name_plural = 'Большие услуги'


class ServicesSmall(models.Model):
    order = models.SmallIntegerField('Сортировка', default=0)
    works = models.ForeignKey(ServicesMain, verbose_name='Маленькая услуга', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='small_service')
    title = models.CharField('Заголовок услуги', max_length=100)
    descr = models.TextField('Описание Услуги')
    icon = models.ForeignKey(ServicesIcon, verbose_name='Иконка услуги', null=True, blank=True,
                             on_delete=models.SET_NULL, related_name='icon_small_service')
    draft = models.BooleanField("Публикация", default=True)

    def __str__(self):
        return "Маленькие услуги"

    class Meta:
        verbose_name = 'Маленькие услуги'
        verbose_name_plural = 'Маленькие услуги'
