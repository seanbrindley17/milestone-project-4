# Generated by Django 5.1.3 on 2025-01-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_is_casual_product_is_competitive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_personalised',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
