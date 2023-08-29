# Generated by Django 4.2.4 on 2023-08-28 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_alter_conta_data_abertura'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cep',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='conta',
            name='data_abertura',
            field=models.DateField(default=datetime.datetime(2023, 8, 28, 19, 7, 1, 737891)),
        ),
    ]
