# Generated by Django 4.0.2 on 2022-04-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_app', '0003_importantpoints_titulo_libro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Img_Books'),
        ),
    ]