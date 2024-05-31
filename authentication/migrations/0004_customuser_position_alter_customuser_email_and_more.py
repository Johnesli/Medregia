# Generated by Django 4.2.11 on 2024-05-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0003_person_pharmacistemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Senior', 'Senior'), ('Member', 'Member'), ('NewUser', 'NewUser')], default='Admin', max_length=20, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', to='auth.group', verbose_name='Groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='other_value',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Other Value'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_num',
            field=models.CharField(blank=True, max_length=15, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pin',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='PIN'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='store_type',
            field=models.CharField(blank=True, choices=[('retailer', 'Retailer'), ('manufacturer', 'Manufacturer'), ('pharmacy', 'Pharmacy'), ('medical', 'Medical'), ('others', 'Others')], max_length=50, null=True, verbose_name='Store Type'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', to='auth.permission', verbose_name='User Permissions'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Username'),
        ),
    ]