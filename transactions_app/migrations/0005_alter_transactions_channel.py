# Generated by Django 5.1.4 on 2024-12-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions_app', '0004_alter_transactions_accountbalance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Channel',
            field=models.CharField(choices=[('ATM', 'ATM'), ('Online', 'Online'), ('Branch', 'Branch')], max_length=50),
        ),
    ]
