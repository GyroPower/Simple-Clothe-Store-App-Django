# Generated by Django 4.2.3 on 2023-09-11 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_brand_2_image_for_clothe_alter_clothes_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image_and_color_of_clothe',
            old_name='cloteh_image',
            new_name='images',
        ),
    ]
