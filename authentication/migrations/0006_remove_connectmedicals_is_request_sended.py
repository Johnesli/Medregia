# Generated by Django 4.2.14 on 2024-07-18 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_connectmedicals_is_request_sended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectmedicals',
            name='is_request_sended',
        ),
    ]
