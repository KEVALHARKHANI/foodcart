# Generated by Django 3.0.6 on 2020-05-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='restro',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
