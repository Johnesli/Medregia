# Generated by Django 4.2.11 on 2024-05-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invclc', '0002_trackingpayment_bill_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
