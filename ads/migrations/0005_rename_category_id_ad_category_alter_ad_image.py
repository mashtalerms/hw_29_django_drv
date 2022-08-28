# Generated by Django 4.0.1 on 2022-08-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_ad_category_id_ad_image_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='category_id',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
