# Generated by Django 3.2.7 on 2022-08-12 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0013_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
    ]