# Generated by Django 2.2.4 on 2019-10-05 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'modelo_Servicio', 'verbose_name_plural': 'tabla_Servicios'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='updated',
            new_name='Actualizado',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='content',
            new_name='Contenido',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='created',
            new_name='Creado',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='Imagen',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='subtitle',
            new_name='Sub-título',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='Título',
        ),
    ]
