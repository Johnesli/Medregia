# Generated by Django 4.2.3 on 2024-03-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_historicalcustomuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.DeleteModel(
            name='HistoricalCustomUser',
        ),
    ]
