# Generated by Django 3.2.7 on 2022-08-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0005_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'primary'), ('SW', 'secondary')], max_length=2),
        ),
    ]
