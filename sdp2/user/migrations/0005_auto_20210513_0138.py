# Generated by Django 3.1.7 on 2021-05-12 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delivery_is_transit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='is_recieved',
            new_name='is_received',
        ),
    ]
