# Generated by Django 4.2.4 on 2023-08-21 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='data_abertura',
            field=models.DateField(default=datetime.datetime(2023, 8, 21, 9, 36, 31, 682590)),
        ),
    ]
