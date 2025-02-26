# Generated by Django 5.1.4 on 2024-12-29 06:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('imagen', models.URLField(blank=True, null=True)),
                ('contenido', models.TextField()),
                ('posdata', models.TextField(blank=True, null=True)),
                ('iframe', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('etiquetas', models.TextField(blank=True, default='[]', null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartas', to=settings.AUTH_USER_MODEL)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cartas_recibidas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Título del poema', max_length=200)),
                ('contenido', models.TextField(help_text='Contenido del poema')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora de creación')),
                ('actualizado_en', models.DateTimeField(auto_now=True, help_text='Fecha y hora de última actualización')),
                ('imagen', models.URLField(blank=True, default='~/assets/img/fondo2.webp', null=True)),
                ('autor', models.ForeignKey(help_text='Usuario que creó el poema', on_delete=django.db.models.deletion.CASCADE, related_name='poemas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Poema',
                'verbose_name_plural': 'Poemas',
                'ordering': ['-creado_en'],
            },
        ),
    ]
