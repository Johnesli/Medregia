# Generated by Django 4.2.9 on 2024-03-25 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invclc', '0022_trackingpayment_paying_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='current_time',
            field=models.TimeField(default=datetime.time(11, 9, 32, 993765)),
        ),
    ]