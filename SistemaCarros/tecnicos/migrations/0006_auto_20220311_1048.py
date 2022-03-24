# Generated by Django 3.2.10 on 2022-03-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tecnicos', '0005_auto_20220308_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnicos',
            name='apellidoTecnico',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tecnicos',
            name='emailTecnico',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tecnicos',
            name='nombreTecnico',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tecnicos',
            name='notasTecnico',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tecnicos',
            name='telTecnico',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='tecnicos',
            name='telTecnico2',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
