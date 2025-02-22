# Generated by Django 5.1.4 on 2024-12-13 18:15

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions_app', '0003_remove_accounts_accountbalance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='AccountBalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='Location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='PreviousTransactionDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='TransactionAmount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='TransactionDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
