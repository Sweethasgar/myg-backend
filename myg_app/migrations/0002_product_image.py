# Generated by Django 4.0 on 2023-03-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myg_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
