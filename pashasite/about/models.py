from django.db import models
from solo.models import SingletonModel


class About(SingletonModel):
    title = models.CharField('Заголовок', max_length=60)
    desr = models.TextField('Описание')
    image = models.ImageField('Избражение', upload_to="image/")

    def __str__(self):
        return "Обо мне"

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'
