# Generated by Django 5.1.6 on 2025-02-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0008_orderpaydb'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdb',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
