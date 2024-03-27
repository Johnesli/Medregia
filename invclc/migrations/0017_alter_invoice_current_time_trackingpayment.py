# Generated by Django 4.2.3 on 2024-03-21 09:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invclc', '0016_alter_invoice_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='current_time',
            field=models.TimeField(default=datetime.time(15, 13, 33, 272172)),
        ),
        migrations.CreateModel(
            name='TrackingPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medical_name', models.CharField(max_length=100)),
                ('Medical_payments', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField(default=django.utils.timezone.now)),
                ('payment_time', models.TimeField(default=datetime.time(15, 13, 33, 272172))),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invclc.modifiedinvoice')),
            ],
        ),
    ]