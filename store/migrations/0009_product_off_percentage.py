# Generated by Django 3.2 on 2021-05-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_off_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='off_percentage',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
