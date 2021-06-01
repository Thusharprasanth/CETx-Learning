# Generated by Django 3.1 on 2021-06-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('category_image', models.ImageField(upload_to='photos/category')),
            ],
        ),
    ]