# Generated by Django 4.0.5 on 2022-06-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_works_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
    ]
