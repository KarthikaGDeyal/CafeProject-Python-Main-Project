# Generated by Django 5.0.7 on 2024-08-01 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdb',
            name='Subject',
        ),
    ]