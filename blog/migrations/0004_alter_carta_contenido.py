# Generated by Django 5.1.4 on 2024-12-30 06:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_carta_etiquetas_alter_carta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
