# Generated by Django 3.1.7 on 2021-05-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datlien', '0011_deliveryboy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryboy',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
