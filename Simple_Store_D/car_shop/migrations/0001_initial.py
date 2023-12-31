# Generated by Django 4.2.3 on 2023-07-21 05:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clothes', '0002_clothes_units'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Clothe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('units', models.IntegerField(default=1)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('clothe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clothes.clothes')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_to_pay', models.FloatField(default=0)),
                ('order_data', models.ManyToManyField(to='car_shop.order_clothe')),
            ],
        ),
    ]
