# Generated by Django 5.0.4 on 2024-08-02 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacoes', '0010_alter_transacao_data_hora_transacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data_hora_transacao',
            field=models.DateField(default=datetime.datetime(2024, 8, 2, 22, 27, 33, 688742, tzinfo=datetime.timezone.utc)),
        ),
    ]