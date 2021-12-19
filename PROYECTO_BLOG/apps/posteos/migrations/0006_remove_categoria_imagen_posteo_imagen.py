# Generated by Django 4.0 on 2021-12-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posteos', '0005_categoria_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='imagen',
        ),
        migrations.AddField(
            model_name='posteo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]