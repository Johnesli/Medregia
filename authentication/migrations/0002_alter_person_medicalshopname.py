# Generated by Django 4.2.14 on 2024-08-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='MedicalShopName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
