# Generated by Django 4.0.5 on 2022-06-17 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_works_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageset',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='imageset',
            name='object_id',
        ),
    ]
