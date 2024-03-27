# Generated by Django 4.2.3 on 2024-03-23 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invclc', '0021_alter_invoice_current_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingpayment',
            name='paying_amount',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='current_time',
            field=models.TimeField(default=datetime.time(17, 3, 22, 986968)),
        ),
        migrations.AlterField(
            model_name='trackingpayment',
            name='Medical_payments',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]