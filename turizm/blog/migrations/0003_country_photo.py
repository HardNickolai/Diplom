# Generated by Django 4.0.5 on 2022-10-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_city_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]