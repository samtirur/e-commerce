# Generated by Django 3.2 on 2021-05-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_addaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='addaddress',
            name='order_note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
