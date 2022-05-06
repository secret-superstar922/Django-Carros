# Generated by Django 3.2.10 on 2022-05-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManoObra', '0017_remove_manoobra_estimate_ids'),
        ('Parte', '0016_remove_parte_estimate_id'),
        ('Pagos', '0009_remove_pagos_estimate'),
        ('Foto', '0006_alter_foto_imagenes'),
        ('Presupuestos', '0014_presupuestos_register_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuestos',
            name='foto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Foto.foto'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='mano_obra',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ManoObra.manoobra'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='pago',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Pagos.pagos'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='parte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Parte.parte'),
        ),
    ]
