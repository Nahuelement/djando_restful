# Generated by Django 3.1.4 on 2022-02-01 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0002_auto_20220126_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='dronecategory',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]