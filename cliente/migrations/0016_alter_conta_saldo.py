# Generated by Django 5.1 on 2024-08-18 16:08

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0015_alter_conta_status_conta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15),
        ),
    ]
