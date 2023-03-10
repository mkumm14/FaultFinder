# Generated by Django 4.1.7 on 2023-03-06 07:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture_height',
            field=models.PositiveIntegerField(default=1000, editable=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_width',
            field=models.PositiveIntegerField(default=1000, editable=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default-profile-pic.png', height_field='picture_height', upload_to='profile_pictures/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])], width_field='picture_width'),
        ),
    ]
