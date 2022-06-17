# Generated by Django 4.0.5 on 2022-06-16 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Подзаголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('prew_image', models.ImageField(upload_to='image/', verbose_name='Превью на главную')),
            ],
            options={
                'verbose_name': 'Работы',
                'verbose_name_plural': 'Работы',
            },
        ),
        migrations.CreateModel(
            name='ImageSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(default=1, null=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('works', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.works', verbose_name='Работа')),
            ],
            options={
                'verbose_name': 'Фото работ',
                'verbose_name_plural': 'Фото работ',
            },
        ),
    ]
