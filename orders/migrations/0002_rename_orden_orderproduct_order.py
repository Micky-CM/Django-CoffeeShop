# Generated by Django 5.1.7 on 2025-03-20 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='orden',
            new_name='order',
        ),
    ]
