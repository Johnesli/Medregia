# Generated by Django 4.2.11 on 2024-05-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invclc', '0003_alter_invoice_payment_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]