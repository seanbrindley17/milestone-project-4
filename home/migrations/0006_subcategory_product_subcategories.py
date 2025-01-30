# Generated by Django 5.1.3 on 2025-01-30 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual', models.BooleanField(blank=True, default=False, null=True)),
                ('training', models.BooleanField(blank=True, default=False, null=True)),
                ('competitive', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.subcategory'),
        ),
    ]
