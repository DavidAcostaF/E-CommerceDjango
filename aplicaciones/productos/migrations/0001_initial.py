# Generated by Django 4.0.4 on 2022-06-22 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrearProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Producto')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('costo', models.CharField(max_length=50, verbose_name='Costo')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='Imagen')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_registro', models.DateField(auto_now=True, verbose_name='Fecha de registro')),
            ],
            options={
                'verbose_name': 'CrearProducto',
                'verbose_name_plural': 'CrearProductos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.crearproducto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.crearproducto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
    ]