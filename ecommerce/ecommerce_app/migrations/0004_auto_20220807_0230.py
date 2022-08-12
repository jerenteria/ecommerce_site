# Generated by Django 3.2.7 on 2022-08-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_auto_20220806_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sweater')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sweater')], default='P', max_length=2),
            preserve_default=False,
        ),
    ]