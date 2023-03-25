# Generated by Django 4.1.4 on 2023-03-25 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='img',
            field=models.ImageField(upload_to='osteo/images', validators=[django.core.validators.validate_image_file_extension], verbose_name='Upload Image'),
        ),
    ]