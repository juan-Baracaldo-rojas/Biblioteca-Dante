# Generated by Django 4.0.2 on 2022-04-23 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria_app', '0002_rename_libro_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantpoints',
            name='Titulo_Libro',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='libreria_app.book'),
        ),
    ]