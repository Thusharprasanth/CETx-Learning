# Generated by Django 3.1 on 2021-06-01 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
    ]