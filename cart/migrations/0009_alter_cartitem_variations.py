# Generated by Django 3.2 on 2021-05-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_variarion_value_variation_variation_value'),
        ('cart', '0008_alter_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
