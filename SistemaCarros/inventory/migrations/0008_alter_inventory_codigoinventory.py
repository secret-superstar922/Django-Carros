# Generated by Django 3.2.10 on 2022-03-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_inventory_fecha_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='codigoInventory',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
