# Generated by Django 4.0.4 on 2022-06-23 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_apellidos_alter_usuario_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': [('permiso_desde_codigo', 'Este es un permiso creado desde codigo'), ('segundo_permiso_codigo', 'Segundo permiso creado desde codigo')]},
        ),
    ]