# Generated by Django 4.0.4 on 2022-05-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0002_company_stock_name_alter_stock_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='amount',
            new_name='total_amount',
        ),
        migrations.AddField(
            model_name='company',
            name='year_of_foundation',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
