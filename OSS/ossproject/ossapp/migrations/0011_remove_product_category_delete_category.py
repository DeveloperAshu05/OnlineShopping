# Generated by Django 4.1 on 2022-08-29 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0010_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
