# Generated by Django 5.0.6 on 2024-07-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_connectmedicals_sender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectmedicals',
            name='sender_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]