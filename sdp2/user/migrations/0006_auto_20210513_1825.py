# Generated by Django 3.1.7 on 2021-05-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210513_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
