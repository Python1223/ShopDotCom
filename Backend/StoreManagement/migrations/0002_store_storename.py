# Generated by Django 3.2.4 on 2023-01-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='storeName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
