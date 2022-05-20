# Generated by Django 4.0.4 on 2022-05-19 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0005_alter_stock_number_of_shares'),
    ]

    operations = [
        migrations.AddField(
            model_name='dividend',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dividends.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dividend',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('number_of_shares', models.DecimalField(decimal_places=10, max_digits=15)),
                ('currency', models.CharField(max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dividends.company')),
            ],
        ),
    ]
