# Generated by Django 4.2.3 on 2024-04-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_person_druglicenesenumber1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DrugLiceneseNumber1',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='DrugLiceneseNumber2',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='MedicalShopName',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='ProprietaryName',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='ProprietaryNumber',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='RegisteredNumber',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='UniqueId',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]