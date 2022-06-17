# Generated by Django 4.0.5 on 2022-06-17 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_imageset_image_alter_imageset_works'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='works',
            name='date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Дата публикации'),
        ),
    ]
