# Generated by Django 3.1.5 on 2021-01-24 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210123_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]