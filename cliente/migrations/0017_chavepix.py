# Generated by Django 5.0.4 on 2024-09-14 22:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0016_alter_conta_saldo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChavePix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('CPF', 'CPF'), ('TEL', 'TELEFONE'), ('E', 'EMAIL'), ('CA', 'CHAVE ALEATÓRIA')], max_length=30)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]