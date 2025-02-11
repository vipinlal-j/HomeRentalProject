# Generated by Django 5.1.6 on 2025-02-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_postdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdb',
            name='Information',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='postdb',
            name='Kitchen',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='postdb',
            name='Rooms',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]
