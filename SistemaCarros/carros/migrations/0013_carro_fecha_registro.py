# Generated by Django 3.2.10 on 2022-02-25 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0012_auto_20220216_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='fecha_registro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
