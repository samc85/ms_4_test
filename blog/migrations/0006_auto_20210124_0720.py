# Generated by Django 3.1.5 on 2021-01-24 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210124_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image_url',
            new_name='images_url',
        ),
    ]
