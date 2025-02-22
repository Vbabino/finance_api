# Generated by Django 5.1.4 on 2024-12-11 21:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions_app', '0002_rename_account_balance_accounts_accountbalance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='AccountBalance',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='CustomerAge',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='CustomerOccupation',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='PreviousTransactionDate',
        ),
        migrations.RemoveField(
            model_name='devices',
            name='IPAddress',
        ),
        migrations.RemoveField(
            model_name='merchants',
            name='Location',
        ),
        migrations.AddField(
            model_name='transactions',
            name='AccountBalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='transactions',
            name='CustomerAge',
            field=models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='transactions',
            name='CustomerOccupation',
            field=models.CharField(default='Other', max_length=50),
        ),
        migrations.AddField(
            model_name='transactions',
            name='IPAddress',
            field=models.GenericIPAddressField(default='0.0.0.0'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='Location',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='transactions',
            name='PreviousTransactionDate',
            field=models.DateTimeField(default='2021-01-01 00:00:00'),
        ),
    ]
