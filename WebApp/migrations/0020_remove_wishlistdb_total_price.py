# Generated by Django 5.0.7 on 2024-09-30 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0019_rename_stock_wishlistdb_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistdb',
            name='Total_price',
        ),
    ]
