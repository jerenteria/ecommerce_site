# Generated by Django 3.2.7 on 2022-08-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0010_auto_20220810_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', to='ecommerce_app.Product'),
        ),
    ]
