# Generated by Django 3.1.7 on 2021-05-18 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20210518_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_boy',
        ),
    ]