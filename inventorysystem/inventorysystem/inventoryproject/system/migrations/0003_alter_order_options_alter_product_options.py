# Generated by Django 4.2.10 on 2024-02-26 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Staff Product'},
        ),
    ]
