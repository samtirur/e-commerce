# Generated by Django 3.2 on 2021-05-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_off_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='off_price',
            field=models.IntegerField(null=True),
        ),
    ]
