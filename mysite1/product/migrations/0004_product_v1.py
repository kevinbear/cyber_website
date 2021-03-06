# Generated by Django 2.1.1 on 2018-09-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_v1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField()),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
