# Generated by Django 2.2.6 on 2020-05-01 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restro',
            name='closetime',
            field=models.TimeField(default=datetime.time(11, 0)),
            preserve_default=False,
        ),
    ]
