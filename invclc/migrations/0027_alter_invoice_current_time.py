# Generated by Django 4.2.3 on 2024-03-25 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invclc', '0026_alter_invoice_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='current_time',
            field=models.TimeField(default=datetime.time(0, 38, 49, 427722)),
        ),
    ]
