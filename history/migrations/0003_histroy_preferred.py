# Generated by Django 3.0.6 on 2020-06-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20200526_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='histroy',
            name='preferred',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
