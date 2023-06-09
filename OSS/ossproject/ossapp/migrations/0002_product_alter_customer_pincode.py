# Generated by Django 4.1 on 2022-08-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
