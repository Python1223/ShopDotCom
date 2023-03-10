# Generated by Django 3.2.4 on 2023-01-18 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProfileManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseListModel',
            fields=[
                ('purchaseListId', models.AutoField(primary_key=True, serialize=False)),
                ('purchaseIdList', models.CharField(default='', max_length=500)),
                ('buyerProfileIns', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ProfileManagement.buyerprofilemodel')),
            ],
        ),
    ]
