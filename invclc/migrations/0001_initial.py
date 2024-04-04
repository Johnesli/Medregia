# Generated by Django 4.2.9 on 2024-04-04 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medical_name', models.CharField(max_length=100)),
                ('Medical_payments', models.DecimalField(decimal_places=2, max_digits=20)),
                ('payment_date', models.DateField(default=django.utils.timezone.now)),
                ('paying_amount', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModifiedInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_pharmacy', models.CharField(max_length=100)),
                ('modified_Invoice_number', models.CharField(max_length=50, unique=True)),
                ('modified_Invoice_date', models.DateField(default=django.utils.timezone.now)),
                ('modified_Total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('modified_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('modified_today_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy_name', models.CharField(max_length=100)),
                ('invoice_number', models.CharField(max_length=50, unique=True)),
                ('invoice_date', models.DateField(default=django.utils.timezone.now)),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('today_date', models.DateField(default=django.utils.timezone.now)),
                ('current_time', models.TimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=50, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('today_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
