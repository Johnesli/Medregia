# Generated by Django 4.2.3 on 2024-05-29 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invclc', '0007_alter_invoice_payment_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_sendername', models.CharField(max_length=20)),
                ('mail_receiver_name', models.CharField(max_length=20)),
                ('mail_receiver_email', models.EmailField(max_length=254)),
                ('mail_receiver_phonenumber', models.CharField(max_length=15)),
                ('mail_receiver_position', models.CharField(choices=[('Admin', 'Admin'), ('Seinor', 'Senior'), ('Member', 'Member'), ('NewUser', 'NewUser')], max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
