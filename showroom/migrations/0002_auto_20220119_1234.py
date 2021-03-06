# Generated by Django 3.2.9 on 2022-01-19 12:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclemodel',
            name='vimage',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='contact',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Please Enter Valid Mobile Number')]),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='fname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Please Enter Valid Name')]),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='lname',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Please Enter Valid Name')]),
        ),
        migrations.AlterField(
            model_name='dealermodel',
            name='dcontact',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Please Enter Valid Mobile Number')]),
        ),
        migrations.AlterField(
            model_name='dealermodel',
            name='dname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Please Enter Valid Name')]),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='scontact',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Please Enter Valid Mobile Number')]),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='sname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Please Enter Valid Name')]),
        ),
    ]
