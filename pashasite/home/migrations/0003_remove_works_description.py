# Generated by Django 4.0.5 on 2022-06-17 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_works_draft_works_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='description',
        ),
    ]
