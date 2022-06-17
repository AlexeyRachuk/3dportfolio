from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class Home(models.Model):
    title = models.CharField('Заголовок', max_length=70)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'


class Works(models.Model):
    title = models.CharField('Название', max_length=70)
    subtitle = models.CharField('Подзаголовок', max_length=100)
    prew_image = models.ImageField('Превью на главную', upload_to="image/")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Публикация", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.url})

    class Meta:
        verbose_name = 'Работы'
        verbose_name_plural = 'Работы'


class ImageSet(models.Model):
    order = models.SmallIntegerField('Сортировка', default=0)
    works = models.ForeignKey(Works, verbose_name='Изображение работы', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='image/', verbose_name='Изображение работы')

    class Meta:
        verbose_name = 'Фото работ'
        verbose_name_plural = 'Фото работ'
