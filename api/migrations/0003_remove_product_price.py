# Generated by Django 5.0.1 on 2024-02-06 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
