# Generated by Django 4.1 on 2022-08-29 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
