# Generated by Django 3.2 on 2021-06-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='userprofile'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
