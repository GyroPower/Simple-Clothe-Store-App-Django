# Generated by Django 4.2.3 on 2023-08-02 03:49

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0006_alter_sizes_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
    ]
