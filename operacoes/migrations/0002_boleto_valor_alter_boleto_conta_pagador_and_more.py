# Generated by Django 4.2.4 on 2023-08-21 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0005_creditcard_alter_conta_data_abertura'),
        ('operacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleto',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='boleto',
            name='conta_pagador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conta_pagador', to='cliente.conta'),
        ),
        migrations.AlterField(
            model_name='boleto',
            name='pagador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pagador', to=settings.AUTH_USER_MODEL),
        ),
    ]
