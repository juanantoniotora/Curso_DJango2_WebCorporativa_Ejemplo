# Generated by Django 2.2.4 on 2019-10-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20191005_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Sub-título')),
                ('content', models.TextField(default='', verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'modelo_Servicio',
                'verbose_name_plural': 'tabla_Servicios',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
