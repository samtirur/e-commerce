# Generated by Django 3.2 on 2021-05-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210511_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images_4',
            field=models.ImageField(default=0, upload_to='photos/products'),
            preserve_default=False,
        ),
    ]