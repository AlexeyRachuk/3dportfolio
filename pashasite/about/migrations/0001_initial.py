# Generated by Django 4.0.5 on 2022-06-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('desr', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Избражение')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
    ]
