# Generated by Django 5.1.6 on 2025-02-11 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_imagedb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
