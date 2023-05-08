# Generated by Django 4.1 on 2022-09-02 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ossapp', '0024_alter_customer_regdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ossapp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ossapp.product')),
            ],
        ),
    ]