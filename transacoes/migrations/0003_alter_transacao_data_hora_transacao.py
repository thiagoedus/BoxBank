# Generated by Django 4.2.4 on 2023-08-21 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0002_alter_transacao_conta_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data_hora_transacao',
            field=models.DateField(default=datetime.datetime(2023, 8, 21, 13, 37, 36, 860715, tzinfo=datetime.timezone.utc)),
        ),
    ]
