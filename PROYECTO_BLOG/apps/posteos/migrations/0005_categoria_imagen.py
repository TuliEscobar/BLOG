# Generated by Django 4.0 on 2021-12-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posteos', '0004_posteo_categorias_alter_categoria_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]
