# Generated by Django 3.2 on 2021-05-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, default=0, max_length=250),
            preserve_default=False,
        ),
    ]
