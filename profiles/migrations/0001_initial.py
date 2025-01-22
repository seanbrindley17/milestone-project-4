# Generated by Django 5.1.3 on 2025-01-22 17:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=30, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=50, null=True)),
                ('county', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
