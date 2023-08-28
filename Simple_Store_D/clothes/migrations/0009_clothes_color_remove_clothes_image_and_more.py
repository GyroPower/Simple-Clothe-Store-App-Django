# Generated by Django 4.2.3 on 2023-08-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0008_colors_color_name_alter_colors_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='color',
            field=models.ManyToManyField(blank=True, to='clothes.colors'),
        ),
        migrations.RemoveField(
            model_name='clothes',
            name='image',
        ),
        migrations.AlterField(
            model_name='clothes',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='clothes.sizes'),
        ),
        migrations.AlterField(
            model_name='sizes',
            name='size',
            field=models.CharField(default='S'),
        ),
        migrations.DeleteModel(
            name='Clothe_image',
        ),
        migrations.AddField(
            model_name='clothes',
            name='image',
            field=models.ImageField(null=True, upload_to='clothes/'),
        ),
    ]
