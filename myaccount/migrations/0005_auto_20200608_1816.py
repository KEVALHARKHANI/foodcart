# Generated by Django 3.0.6 on 2020-06-08 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0004_auto_20200608_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
