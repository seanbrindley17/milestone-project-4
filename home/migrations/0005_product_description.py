# Generated by Django 5.1.3 on 2025-01-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_for_training_product_reverse_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
