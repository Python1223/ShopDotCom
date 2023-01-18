# Generated by Django 3.2.4 on 2023-01-18 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerProfileModel',
            fields=[
                ('userIns', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('profileType', models.CharField(default='Buyer', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SellerProfileModel',
            fields=[
                ('userIns', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('storeId', models.IntegerField(default=-1)),
                ('storeName', models.CharField(max_length=50)),
                ('profileType', models.CharField(default='Seller', max_length=10)),
            ],
        ),
    ]
