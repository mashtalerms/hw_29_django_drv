# Generated by Django 4.0.1 on 2022-08-21 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_rename_category_ad_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author',
            new_name='author_id',
        ),
    ]
