# Generated by Django 2.1.1 on 2018-09-07 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='content',
        ),
    ]
