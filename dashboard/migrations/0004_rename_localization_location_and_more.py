# Generated by Django 5.0.6 on 2024-06-13 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_localization_alter_product_photo_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Localization',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='localization',
            new_name='location',
        ),
    ]