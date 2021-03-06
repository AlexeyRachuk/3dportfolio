# Generated by Django 4.0.5 on 2022-06-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Публикация'),
        ),
        migrations.AddField(
            model_name='works',
            name='url',
            field=models.SlugField(default=1, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]
