# Generated by Django 3.2.10 on 2022-06-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReporteGanancias', '0002_reportetechnician'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportetechnician',
            name='register_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
