# Generated by Django 2.2.1 on 2019-08-27 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('transaction_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('frequency_of_transactions', models.IntegerField(default=0)),
                ('vol_of_spending', models.IntegerField(default=0)),
                ('period', models.IntegerField(default=0)),
                ('loyalty_duration', models.IntegerField(default=0)),
                ('valid_from', models.DateField(default=datetime.date.today)),
                ('valid_to', models.DateField(default=datetime.date.today)),
                ('money', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('redemp_max', models.IntegerField()),
            ],
        ),
    ]