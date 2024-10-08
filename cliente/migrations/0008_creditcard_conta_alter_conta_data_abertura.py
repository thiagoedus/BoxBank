# Generated by Django 4.2.4 on 2023-08-24 12:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_alter_conta_data_abertura_alter_creditcard_limite'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcard',
            name='conta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.conta'),
        ),
        migrations.AlterField(
            model_name='conta',
            name='data_abertura',
            field=models.DateField(default=datetime.datetime(2023, 8, 24, 9, 1, 57, 494515)),
        ),
    ]
